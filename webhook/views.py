import os

import mercadopago
from django.http import HttpResponse, JsonResponse

sdk = mercadopago.SDK(os.environ.get('ACCESS_TOKEN'))

# Create your views here.


def home(request):
    return HttpResponse("Hello, Django!")


def methodsPayments(request):
    payment_methods_response = sdk.payment_methods().list_all()
    payment_methods = payment_methods_response["response"]
    return JsonResponse(payment_methods, safe=False)
