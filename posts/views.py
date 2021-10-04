
from django.shortcuts import render
#from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import posts




posts = [

{
    'title':'Python',
    'users':{'name':'Nico lopez',
    'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDGKhWzXmC26Sjj7A_e8nmBx99A1exlYEI-w&usqp=CAU'
        },
        'timestamp':datetime.now().strftime('%b %d %dth, %Y - %H:%M hrs'),
         'photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHc5L89-K9Hb44e-4w2RutP91Tcv4Og8BiPQ&usqp=CAU'

},
{
    'title':'Python',
    'users':{'name':'Jose Barrera',
    'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDGKhWzXmC26Sjj7A_e8nmBx99A1exlYEI-w&usqp=CAU'
        },
        'timestamp':datetime.now().strftime('%b %d %dth, %Y - %H:%M hrs'),
         'photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHc5L89-K9Hb44e-4w2RutP91Tcv4Og8BiPQ&usqp=CAU'

},
{
    'title':'Python',
    'users':{'name':'Alvaro De La Rosa',
    'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDGKhWzXmC26Sjj7A_e8nmBx99A1exlYEI-w&usqp=CAU'
        },
        'timestamp':datetime.now().strftime('%b %d %dth, %Y - %H:%M hrs'),
         'photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHc5L89-K9Hb44e-4w2RutP91Tcv4Og8BiPQ&usqp=CAU'

},
{
    'title':'Python',
    'users':{'name':'Facundo Chacon',
    'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDGKhWzXmC26Sjj7A_e8nmBx99A1exlYEI-w&usqp=CAU'
        },
        'timestamp':datetime.now().strftime('%b %d %dth, %Y - %H:%M hrs'),
         'photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHc5L89-K9Hb44e-4w2RutP91Tcv4Og8BiPQ&usqp=CAU'

},
]






def list_posts(Request):
    return render(Request,'feed.html',{'posts':posts})
    
