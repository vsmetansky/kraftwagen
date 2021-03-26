import logging

from django.core.exceptions import FieldError, SuspiciousOperation
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from showroom.models import Employee, Car, Client

logger = logging.getLogger(__name__)


def convert_type(val):
    try:
        return int(val)
    except ValueError:
        return val


async def index(request):
    return render(request, 'index.html')


def employees(request):
    try:
        params = {k: convert_type(v) for k, v in request.GET.items()}
        e = Employee.objects.filter(**params).select_related('fullname', 'position')
        return render(request, 'employees.html', dict(employees=e))
    except (FieldError, ValueError):
        raise SuspiciousOperation()


@require_http_methods(['GET', 'POST'])
def cars(request):
    try:
        params = {k: convert_type(v) for k, v in request.GET.items()}
        c = Car.objects.filter(**params).select_related(
            'manufacturer', 'body_type', 'employee', 'facility_1', 'facility_2', 'facility_3')
        return render(request, 'cars.html', dict(cars=c))
    except (FieldError, ValueError):
        raise SuspiciousOperation()


def orders(request):
    try:
        params = {k: convert_type(v) for k, v in request.GET.items()}
        o = Client.objects.filter(**params).select_related('fullname', 'car', 'employee')
        t = sum(order.car.price for order in o)
        return render(request, 'orders.html', dict(orders=o, total=t))
    except (FieldError, ValueError):
        raise SuspiciousOperation()
