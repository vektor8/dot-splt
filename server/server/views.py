from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from server.db import create_new_bill, create_new_user
import json
from server.ocr import img_to_bill
from server.models import Bill, Payments, Product, User
from server.serializers import ProductSerializer


@api_view(http_method_names=['GET'])
@csrf_exempt  # To exempt from default requirement for CSRF tokens to use postman
def HelloWorldView(request):
    return HttpResponse("Hello World!")


@api_view(http_method_names=['POST'])
def authenticate(request): 
    params = json.loads(request.body.decode())
    user = User.objects.filter(name=params['name'])
    id = -1
    if len(user) == 0:
        id = create_new_user(params['name'])
    else:
        id = user[0].id
    response = {"user_id":id}
    return Response(response)


@api_view(http_method_names=['POST'])
def upload_bill(request):
    decoded = request.POST
    file = request.FILES['bill']
    file_name = default_storage.save(file.name, file)
    file = default_storage.open(file_name)
    file_url = default_storage.url(file_name)
    import os
    from server.settings import BASE_DIR
    file_path = os.path.join(BASE_DIR, file_url[1:])
    products = img_to_bill(file_path)
    bill_id = create_new_bill(decoded['author'], products)
    return Response(get_products_response(bill_id))


def get_products_response(billid):
    bill = Bill.objects.get(pk=billid)
    products = Product.objects.filter(bill_id=bill)
    products = [ProductSerializer(p).data for p in products]
    response = {"billid": billid, "products": products}
    return response


@api_view(http_method_names=['GET'])
def get_bill(request):
    return Response(get_products_response(request.GET['billid']))


@api_view(http_method_names=['POST'])
def edit_bill(request):
    user = User.objects.get(pk=request.POST("userid"))
    bill = Bill.objects.get(pk=request.POST['billid'])
    products = request.POST['products']
    for p in products:
        product = Product(pk=p['id'])
        product.update(product.quatity - p['quantity'])
        product.save()
        payment = Payments(user_id=user, product_id=product, quantity=p["quantity"])
        payment.save()
    return Response(get_products_response(request.POST['billid']))


