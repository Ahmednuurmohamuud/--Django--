from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def input(request):
    return render(request, "basic.html")

def add(request):
    try:
        a = request.GET.get('t1')
        b = request.GET.get('t2')

        x = int(a)
        y = int(b)
        z = x + y

        return HttpResponse(f"<html><body bgcolor=blue>Sum is: {z}</body></html>")
    except (ValueError, TypeError):
        return HttpResponse("<html><body bgcolor=red>Invalid input. Please enter valid numbers.</body></html>")


# def add(request):
#     a = request.POST['t1']
#     b = request.POST['t2']

#     x = int(a)
#     y = int(b)
#     z = x+y

#     return HttpResponse("<html><body bgcolor=blue> Sum is :"+str(z)+" </body></html>")