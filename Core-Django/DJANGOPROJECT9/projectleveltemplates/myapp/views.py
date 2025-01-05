from django.shortcuts import render
from django.shortcuts import render

import datetime
from myapp.models import Programmer

# Create your views here.

def home(request):    
    date = datetime.datetime.now()
    my_dict ={"insert_date":date}
    return render(request, 'mywebsitepage1.html', context = my_dict)


def starbucks_view(request):
    return render(request, 'Green1.html')

def tourism(request):    
    return render(request, 'tourism2.html')

def beach(request):    
    return render(request, 'beach.html')

def children(request):    
    return render(request, 'children.html')




def programmerspage(request):
    data = Programmer.objects.all()
    my_dict = {"Programmers":data}
    
    return render(request, 'programmerswebpage.html',context=my_dict)