from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from server.db import create_new_user
import json

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
    render

