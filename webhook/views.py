import json
import os

import mercadopago
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Notification

sdk = mercadopago.SDK(os.environ.get('ACCESS_TOKEN'))

# Create your views here.


def home(request):
    return HttpResponse("Hello, Django!")


def methodPix(request):
    payment_data = {
        "transaction_amount": 100,
        "description": "Título do produto",
        "payment_method_id": "pix",
        "notification_url": "https://ebd6-45-237-1-170.ngrok-free.app/notification",
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


@csrf_exempt
def notification(request):
    if request.method == "POST":
        data = json.loads(request.body)
        notification = Notification(
            data_id=data["data"]["id"],
            action=data["action"],
            type=data["type"],
        )
        notification.save()
        return HttpResponse(status=200)

    return HttpResponse(status=404)
