from django.shortcuts import render

def home(request):
    return render(request, 'appdjango/home.html')

def pagina2(request):
   return render(request, "appdjango/pagina2.html")