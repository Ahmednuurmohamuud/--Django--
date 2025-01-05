from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

import datetime
from myapp.models import Programmer, SoftwareDevelopers

import  faker 
fake = faker.Faker()

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
    print("Hello All")

    # for i in range(8,11):
    #     pgno = i
    #     pgname = "Aliyabhat"+str(i)
    #     pgsal = 50000
    #     pgaddr = "Mumbai"

        # Programmer(
        #     pgno =  pgno,
        #     pgname = pgname,
        #     pgsal =  pgsal,
        #     pgaddr = pgaddr
        # ).save()

    Programmer(
            pgno =  11,
            pgname = "nabhil",
            pgsal =  500000,
            pgaddr = "somalia"
        ).save()

    return render(request, 'children.html')


def adding_bulkdata_view(request):
    for i in range(500):
        pass
      
    return HttpResponse("Bulk Data Saved")


def programmerspage(request):
    # data = Programmer.objects.all()
    data = SoftwareDevelopers.objects.all()
    my_dict = {"Programmers":data}
    
    return render(request, 'programmerswebpage.html',context=my_dict)
    