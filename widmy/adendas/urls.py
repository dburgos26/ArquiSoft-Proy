from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.adendas_view, name='adendas_view'),
    path('<int:identificador>/', views.adenda_view, name='adenda_view'),
]