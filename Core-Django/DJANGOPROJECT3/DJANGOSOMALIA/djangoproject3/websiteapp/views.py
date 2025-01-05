from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    return HttpResponse()

def aboutus(request):
    return HttpResponse("""<html><body bgcolor="green"><br><br><center><h1>ABOUT US</h1></center><body></html>""")

def gallery(request):
    return HttpResponse("""<html><body bgcolor="purple"><br><br><center><h1>GALLERY</h1></center><body></html>""")

def loginpage(request):
    return HttpResponse("""<html><body bgcolor="red"><br><br><center><h1>LOGIN PAGE</h1></center><body></html>""")

def contactus(request):
    return HttpResponse("""<html><body bgcolor="pink"><br><br><center><h1>CONTACT US</h1></center><body></html>""")