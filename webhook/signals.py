import os

import mercadopago
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Notification, Payments

sdk = mercadopago.SDK(os.environ.get('ACCESS_TOKEN'))


@receiver(post_save, sender=Notification)
def notification(sender, instance, created, **kwargs):
    if created and instance.type == "payment" and instance.action == "payment.updated":
        data_id = instance.data_id
        payment_response = sdk.payment().get(data_id)
        paymentupdate = Payments.objects.get(payment_id=data_id)
        paymentupdate.date_last_updated = payment_response["response"]["date_last_updated"]
        paymentupdate.date_approved = payment_response["response"]["date_approved"]
        paymentupdate.status = payment_response["response"]["status"]
        paymentupdate.save()
