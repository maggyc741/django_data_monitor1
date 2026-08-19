from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#Importe el paquete requests y el archivo from django.conf import settings.
import requests
from django.conf import settings

from django.contrib.auth.decorators import login_required

#Cree un diccionario data con el título del Dashboard.
#Pase el diccionario como contexto al renderizar la plantilla index.html.

@login_required

def index(request):

	#Realice una solicitud GET a la API de JSONPlaceholder para obtener una lista de publicaciones.

	response =  requests.get(settings.API_URL) #URL DE LA API
	posts = response.json() #Convierte la respuesta en formato JSON a un objeto de Python (lista de publicaciones)

	#Agregue la entrada total_responses al diccionario data.
	total_responses = len(posts)
	#Limite a 10 las publicaciones que se mostrarán en la tabla.
	table_posts = posts[:10]

	data = {
		'title': "Landing Page' Dashboard",
		'total_responses': total_responses,
		'posts': table_posts,
		'displayed_responses': len(table_posts),
	}

	return render(request, 'dashboard/index.html', data)


