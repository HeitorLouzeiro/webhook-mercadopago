from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('payments/', views.payments, name='payments'),
    path('method-pix/', views.methodPix, name='methodPix'),
    path('notification', views.notification, name='notification'),
    path('payment-status/', views.paymentStatus, name='paymentStatus'),
    path('payment-get-payment/', views.paymentGetPayment,
         name='paymentGetPayment'),
]
