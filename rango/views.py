from django.shortcuts import render

#Import the Category Model
from rango.models import Category

# Create your views here.
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage' : "Crunchy, creamy, cooke, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
	

def about(request):
   # return HttpResponse("Rango says here is the about page. view <a href='/rango/'>Index</a>")
   context_dict = {'boldmessage': "This tutorial has been put together by Oliver Begley"}
   return render(request, 'rango/about.html', context=context_dict)



