from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def adminconsole(request):
    data = """ 
    <html>
    <body bgcolor=black><center>
    <h1><span style=background-color:yellow;>Welcome To Admin Dashboard</span></h1></center>
    <b style="color:white;"><p>Admin Name: Nabil</p>
    <p>Admin Name: Nabil2 </p></b>

    </body> 
    </html>
    """
    return HttpResponse(data)


def adminemps(request):
    data = """ 
    <html>
    <body bgcolor=black><center>
    <h1><span style=background-color:yellow;>Welcome To Admin Employess</span></h1></center>
    <b style="color:white;"><p>Admin Name: Nabil</p>
    <p>Admin Name: Nabil2 </p></b>

    </body> 
    </html>
    """
    return HttpResponse(data)