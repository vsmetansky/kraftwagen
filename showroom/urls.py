from django.urls import path
from django.contrib.auth.views import LoginView

from showroom import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('employees/', views.employees, name='employees'),
    path('cars/', views.cars, name='cars'),
    path('orders/', views.orders, name='orders'),
]
