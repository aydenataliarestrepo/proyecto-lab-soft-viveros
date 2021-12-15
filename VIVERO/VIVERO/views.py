#Vistas que permiten dar una respueta HTTP 

from django.http import HttpResponse 

#--------Primera vista-------#

#Request: Para realizar peticiones 

#HTTPResponse: Para enviar la respuesta usando el protocolo HTTP 

#Definimos la vista_
def bienvenida(request):    #Pasamos un objeto como primer argumento 
    return HttpResponse("Bienvenido a nuestro vivero")