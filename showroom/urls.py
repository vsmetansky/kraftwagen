from django.urls import path

from showroom import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees, name='employees'),
    path('cars/', views.cars, name='cars'),
    path('orders/', views.orders, name='orders'),
]
