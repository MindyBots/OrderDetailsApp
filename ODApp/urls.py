# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('list', views.extract_orders, name='extract_orders'),
]
