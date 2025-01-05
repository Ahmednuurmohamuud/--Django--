from django.shortcuts import render
from django.http import HttpResponse





def getinput(request):
    print("request: ",request)
    return render(request, "getform.html") #submitting form through get request
    

def postinput(request):
    print("request: ",request)
    return render(request, "postform.html") #submitting form through post request



def add(request):
    print("request: ",request)
    if request.method == "GET":


        a = request.GET['t1']
        b = request.GET['t2']

        x = int(a)
        y = int(b)

        z = x+y

        return HttpResponse(" <html><body>Form IF BLOCK sum is    :"+str(z)+"  </body></html>")
    else:
        a = request.POST['t1']
        b = request.POST['t2']


        x = int(a)
        y = int(b)


        z = x+y

        return HttpResponse("<html><body>Form IF BLOCK sum is    :"+str(z)+"   </body></html>")


# Create your views here.
