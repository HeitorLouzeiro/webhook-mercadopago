from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('method-pix/', views.methodPix, name='methodPix'),
    path('notification', views.notification, name='notification'),
]
