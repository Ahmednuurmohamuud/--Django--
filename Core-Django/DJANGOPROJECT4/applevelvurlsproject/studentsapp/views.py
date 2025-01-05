from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def workspace(request):
    data = """ 
    <html>
    <body bgcolor=navy><center>
    <h1><span style=background-color:yellow;>Welcome To Students Page</span></h1></center>
    <b style="color:white;"><p>Student Name: Elon</p>
    <p>Student Name: Messi </p></b>

    </body> 
    </html>
    """
    return HttpResponse(data)