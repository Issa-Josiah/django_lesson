from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Welcome(request):
    return HttpResponse("Hello fam, Welcome to the First App!")
def Template(request):
    return render(request, 'index.html')
