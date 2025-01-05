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
    return render(request, 'homepage.html')

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


# def adding_bulkdata_view(request):

#     SoftwareDevelopers(
#         first_name = "Elon",
#         last_name = "Musk",
#         salary = "60000",
#         email = "musk@gmail.com",
#         company = "BSE",
#         job = "SDE",
#         location = "USA",
#         address ="A block, polt no 202, east street, penselvnia, USA"
#     ).save()      
      
#     return HttpResponse("Bulk Data Saved")


def adding_bulkdata_view(request):
    for i in range(500):
        fn = fake.first_name()
        last_name = fake.last_name()
        salary = fake.random_element(elements=(100000,125000,200000,50000,75000))
        email = fake.email()
        company = fake.random_element(elements=("SpaceX","Google","Microsoft","IBM","OpenAI","NASA"))
        job = fake.random_element(elements=("Programmer","Manager","CEO","Tester","TeamLead","DB Admin","Software Engineer"))
        location = fake.random_element(elements=("Hyderbad","Bangalore","Somalia","Mumbai","Mogadisu","Delhi"))
        address = fake.address()
        
        SoftwareDevelopers(
                first_name = fn,
                last_name = last_name,
                salary = salary,
                email = email,
                company = company,
                job = job,
                location = location,
                address = address
        ).save()       

    return HttpResponse("Sucessfully 10 Records inserted into the SoftwareDevelopers Table.")


def programmerspage(request):
    # data = Programmer.objects.all()
    data = SoftwareDevelopers.objects.all()
    my_dict = {"Programmers":data}
    
    return render(request, 'programmerswebpage.html',context=my_dict)


def somalia_data(request): 
    # data = SoftwareDevelopers.objects.all()     
    #  data = SoftwareDevelopers.objects.filter(company="Google") 
    
    # data = SoftwareDevelopers.objects.filter(location="Somalia") & SoftwareDevelopers.objects.filter(company="Google") 

    if request.method == "POST":
        cmp = request.POST.get('company')
        data = SoftwareDevelopers.objects.filter(location="Somalia") & SoftwareDevelopers.objects.filter(company=cmp)
        my_dict = {"Programmers":data}

    else:
        data = SoftwareDevelopers.objects.filter(location="Somalia") 
        my_dict = {"Programmers":data} 

   
    return render(request, 'somalia_data.html',context=my_dict)


def mogadisu_data(request): 
    if request.method == "POST":
        cmp = request.POST.get('company')
        data = SoftwareDevelopers.objects.filter(location="Mogadisu") & SoftwareDevelopers.objects.filter(company=cmp)
        my_dict = {"Programmers":data}
    else:
        data = SoftwareDevelopers.objects.filter(location="Mogadisu") 
        my_dict = {"Programmers":data}    
    return render(request, 'mogadisu_data.html',context=my_dict)


def hyderabad_data(request): 
    if request.method == "POST":
        cmp = request.POST.get('company')
        data = SoftwareDevelopers.objects.filter(location="Hyderbad") & SoftwareDevelopers.objects.filter(company=cmp)
        my_dict = {"Programmers":data}
    else:
        data = SoftwareDevelopers.objects.filter(location="Hyderbad") 
        my_dict = {"Programmers":data}    
    return render(request, 'hyderabad_data.html',context=my_dict)

def mumbai_data(request): 
    if request.method == "POST":
        cmp = request.POST.get('company')
        data = SoftwareDevelopers.objects.filter(location="Mumbai") & SoftwareDevelopers.objects.filter(company=cmp)
        my_dict = {"Programmers":data}
    else:
        data = SoftwareDevelopers.objects.filter(location="Mumbai") 
        my_dict = {"Programmers":data}    
    return render(request, 'mumbai_data.html',context=my_dict)