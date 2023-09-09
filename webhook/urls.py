from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('methods-payments/', views.methodsPayments, name='methodsPayments'),
]
