from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("""<html><center><h1>My Website</h1></center></html>""")