from django.urls import path
from olist.core import views
urlpatterns = [
    path('', views.autores, name='autores')
]
