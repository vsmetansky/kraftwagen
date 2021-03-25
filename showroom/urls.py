from django.urls import path

from showroom import views

urlpatterns = [
    path('', views.index, name='index'),
]
