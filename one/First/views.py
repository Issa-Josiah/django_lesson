from django.shortcuts import render
from django.http import HttpResponse
from .models import Fist


# Create your views here.
def Welcome(request):
    return HttpResponse("Hello fam, Welcome to the First App!")
def Template(request):
    context = {'plant': 'Amigos'}
    return render(request, 'First/index.html', context)
def Dashboard(request):
    allfists = Fist.objects.all().values()
    context = {'allfists': allfists}
    return render(request, 'First/Fist.html',context)
def details(request):
    allfists = Fist.objects.all().values()
    context = {'allfists':allfists}
    return render(request, 'First/fist_details.html', context)