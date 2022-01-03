from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from server.db import create_new_bill, create_new_user
import json
from server.ocr import img_to_bill
from server.models import Bill, Product
from server.serializers import ProductSerializer

@api_view(http_method_names=['GET'])
@csrf_exempt ## To exempt from default requirement for CSRF tokens to use postman
def HelloWorldView(request):
    return HttpResponse("Hello World!")


@api_view(http_method_names=['POST'])
def new_user(request):
    decoded = request.body.decode().strip()
    params=json.loads(decoded)
    id = create_new_user(params['name'])
    response = {}
    response['user_id'] = id
    return Response(json.dumps(response))


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
    create_new_bill(decoded['author'], products)
    return Response(products)


@api_view(http_method_names=['GET'])
def get_bill(request):
    bill = Bill.objects.get(pk=request.GET['billid'])
    products = Product.objects.filter(bill_id=bill)
    products = [ProductSerializer(p).data for p in products]
    return Response(products)


    
