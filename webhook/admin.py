from django.contrib import admin

from .models import Notification, Payments

# Register your models here.
admin.site.register(Notification)
admin.site.register(Payments)
