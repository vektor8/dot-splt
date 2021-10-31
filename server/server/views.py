from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt ## To exempt from default requirement for CSRF tokens to use postman
def HelloWorldView(request):

    if (request.method == "GET"):
        return HttpResponse("Hello World!")