import json
import os
import time

import mercadopago
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import Notification, Payments

sdk = mercadopago.SDK(os.environ.get('ACCESS_TOKEN'))

# Create your views here.


def home(request):
    template = "webhook/pages/home.html"
    return render(request, template)


def payments(request):
    template = "webhook/pages/payments.html"
    payments = Payments.objects.all().order_by('-date_last_updated')
    context = {
        "payments": payments
    }
    return render(request, template, context)


def methodPix(request):
    payment_data = {
        "transaction_amount": 100,
        "description": "Título do produto",
        "payment_method_id": "pix",
        "notification_url": "https://b19a-45-237-1-170.ngrok-free.app/notification",
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
    paymentsave = Payments(
        first_name=payment["payer"]["first_name"],
        last_name=payment["payer"]["last_name"],
        email=payment["payer"]["email"],
        idetification_type=payment["payer"]["identification"]["type"],
        idetification_number=payment["payer"]["identification"]["number"],
        payment_id=payment["id"],
        description=payment["description"],
        date_approved=payment["date_approved"],
        date_of_expiration=payment["date_of_expiration"],
        date_last_updated=payment["date_last_updated"],
        payment_method_id=payment["payment_method_id"],
        status=payment["status"],
        amount=payment["transaction_amount"],
    )
    paymentsave.save()

    return redirect('payments')


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


def paymentStatus(request):

    payment_id = request.GET.get('payment_id')
    payment_data = {
        "status": "cancelled"
    }
    payment_response = sdk.payment().update(payment_id, payment_data)
    payment = payment_response["response"]

    # time to refresh the page
    time.sleep(2)
    return redirect('payments')


def paymentGetPayment(request):
    payment_id = 1317778667
    payment_response = sdk.payment().get(payment_id)
    payment = payment_response["response"]
    return JsonResponse(payment, safe=False)
