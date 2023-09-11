from django.db import models

# Create your models here.


class Notification(models.Model):
    data_id = models.CharField(max_length=11)
    action = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.data_id + " - " + self.date_created.strftime("%d/%m/%Y %H:%M:%S")


class Payments(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100)
    idetification_type = models.CharField(max_length=10)
    idetification_number = models.CharField(max_length=20)
    payment_id = models.CharField(max_length=11)
    description = models.CharField(max_length=100)
    date_approved = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_of_expiration = models.DateTimeField(null=True, blank=True)
    payment_method_id = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.email + " - " + self.payment_id + " - " + self.status
