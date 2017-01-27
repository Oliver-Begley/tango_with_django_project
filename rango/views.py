from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage' : "Crunchy, creamy, cooke, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
	
def about(request):
	context_dict = {}
	return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/'>Index</a>")
	
	



