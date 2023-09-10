import os

import mercadopago
from django.http import HttpResponse, JsonResponse

sdk = mercadopago.SDK(os.environ.get('ACCESS_TOKEN'))

# Create your views here.


def home(request):
    return HttpResponse("Hello, Django!")


def methodPix(request):
    payment_data = {
        "transaction_amount": 100,
        "description": "Título do produto",
        "payment_method_id": "pix",
        "payer": {
            "email": "UserTest@gmail.com",
            "first_name": "Test",
            "last_name": "User",
            "identification": {
                "type": "CPF",
                "number": "191191191-00"
            },
            "address": {
                "zip_code": "06233-200",
                "street_name": "Av. das Nações Unidas",
                "street_number": "3003",
                "neighborhood": "Bonfim",
                "city": "Osasco",
                "federal_unit": "SP"
            }
        }
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    return JsonResponse(payment, safe=False)
