
from django.shortcuts import render
#from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import posts




posts = [

{
    'title':'Python Django',
    'users':{'name':'Nico lopez',
    'picture': './/imagenes/icono.jpg'
        },
        'timestamp':datetime.now().strftime('%b %d %dth, %Y - %H:%M hrs'),
         'photo':'https://techgenies.com/wp-content/uploads/2021/04/python-django-techgenies-bolsa-de-trabajo.jpg'

},
{
    'title':'Estudiando Python',
    'users':{'name':'Jose Barrera',
    'picture':  ''
        },
        'timestamp':datetime.now().strftime('%b %d %dth, %Y - %H:%M hrs'),
         'photo':'https://www.becas-santander.com/content/dam/becasmicrosites/blog/lenguaje-programacion.jpeg'

},
{
    'title':'GeneXus',
    'users':{'name':'Alvaro De La Rosa',
    'picture': '..//imagenes/icono.jpg'
        },
        'timestamp':datetime.now().strftime('%b %d %dth, %Y - %H:%M hrs'),
         'photo':'https://pbs.twimg.com/profile_images/1318526866307821568/hjWN2taM.jpg'

},
{
    'title':'C#',
    'users':{'name':'Facundo Chacon',
    'picture':  '/imagenes/icono.jpg'
        },
        'timestamp':datetime.now().strftime('%b %d %dth, %Y - %H:%M hrs'),
         'photo':'https://aspnetcoremaster.com/img/csharp.webp'

},
]






def list_posts(Request):
    return render(Request,'feed.html',{'posts':posts})
    
