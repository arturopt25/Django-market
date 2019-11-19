from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request, "login.html", {})

def register_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request, "registro.html", {})

def cart_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request, "grid.html", {})