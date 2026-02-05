from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def about(request):
    # return HttpResponse("<h1>Welcome to About Page</h1>")
    return render(request, 'movie/about.html')

    

def home (request):
    # return HttpResponse("<h1>Welcome to Home Page</h1>")
    # return render( request, 'home.html')
    return render( request, 'home.html', {'name':'Mariana Patiño'})