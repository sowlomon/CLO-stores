from django.shortcuts import render
from django.http import HttpResponse
from .models import Clothing


def home(request):
    Cloth = Clothing.objects.all()
    return render(request,'home.html', {'Clothing':Cloth})


def trending(request):
    return HttpResponse('TRENDING')

