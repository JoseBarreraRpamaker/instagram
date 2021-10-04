from django.urls import path
from django.http import HttpResponse
from datetime import datetime

from django.urls.converters import register_converter



def hello(Request):
    now = datetime.now().strftime('%b,%dth,%Y - %H:%M hors')
    return HttpResponse('hola la fecha de hoy es {now}'.format(now=str(now)))


def hi(Request):
    return HttpResponse('hola como estan')    


def say_hi(Request,name,age):
    if age < 12:
        message = 'sorry {}, la edad deve de ser mayor a 12'.format(name)
    else:
        message = 'hola {}, Welcome to isnta'.format(name) 
    return HttpResponse(message)    