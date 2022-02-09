from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def porf(request):
  return render(request,'porf.html')
