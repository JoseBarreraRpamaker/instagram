from django.shortcuts import render
from django.http import HttpResponse

import posts



def list_posts(Request):
    posts = [1,2,3,4]
    return HttpResponse(str(posts))

