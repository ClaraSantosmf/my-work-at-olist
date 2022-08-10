from django.urls import path
from olist.core import views

# app_name = 'core'

urlpatterns = [
    path('autores/', views.autores, name='lista-autores')
]
