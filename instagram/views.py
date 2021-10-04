from django.urls import path
from django.http import HttpResponse
from datetime import datetime



def hello(Request):
    now = datetime.now()
    return HttpResponse('hola la fecha de hoy es {now}'.format(now=str(now)))