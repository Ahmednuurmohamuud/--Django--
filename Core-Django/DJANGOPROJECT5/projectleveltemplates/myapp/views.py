from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):    
    # return HttpResponse(data)
    return render(request, 'mywebsitepage1.html')

def starbucks_view(request):
    return render(request, 'Green1.html')

def tourism(request):    
    return render(request, 'tourism2.html')