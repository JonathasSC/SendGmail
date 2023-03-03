from django.urls import path
from . import views

urlpatterns = [
    path('', views.emailList, name='email-list'),
]