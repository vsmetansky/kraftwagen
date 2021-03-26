import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import FieldError, SuspiciousOperation
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from showroom.forms import SignUpForm
from showroom.models import Employee, Car, Order


def convert_type(val):
    try:
        return int(val)
    except ValueError:
        return val


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/showroom/login/')
def logout(request):
    auth.logout(request)
    return redirect('signup')


@login_required(login_url='/showroom/login/')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/showroom/login/')
def employees(request):
    try:
        params = {k: convert_type(v) for k, v in request.GET.items()}
        e = Employee.objects.filter(**params).select_related('fullname', 'position')
        return render(request, 'employees.html', dict(employees=e))
    except (FieldError, ValueError):
        raise SuspiciousOperation()


@login_required(login_url='/showroom/login/')
def cars(request):
    try:
        params = {k: convert_type(v) for k, v in request.GET.items()}
        c = Car.objects.filter(**params).select_related(
            'manufacturer', 'body_type', 'employee', 'facility_1', 'facility_2', 'facility_3')
        return render(request, 'cars.html', dict(cars=c))
    except (FieldError, ValueError):
        raise SuspiciousOperation()


@login_required(login_url='/showroom/login/')
def orders(request):
    try:
        params = {k: convert_type(v) for k, v in request.GET.items()}
        o = Order.objects.filter(**params).select_related('fullname', 'car', 'employee')
        t = sum(order.car.price for order in o)
        return render(request, 'orders.html', dict(orders=o, total=t))
    except (FieldError, ValueError):
        raise SuspiciousOperation()
