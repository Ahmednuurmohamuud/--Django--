from django.shortcuts import render
from django.views.generic import View #listview create delete  authentication
from django.http import HttpResponse

# Create your views here.

class GetInput(View):
    def get(self,request):        
        return render(request,'getform.html')


class PostInput(View):
    def get(self,request):
        return render(request,'postform.html')


class Add(View): #GET/POST

    def get(self,request):
        a = request.GET['t1']
        b = request.GET['t2']
        x = int(a)
        y = int(b)
        z = x+y
        return HttpResponse("<html><body>IM FROM GET METHOD BLOCK <br> Sum is  :"+str(z)+" </body></html>")
    
    def post(self, request):
        a = request.POST['t1']
        b = request.POST['t2']
        x = int(a)
        y = int(b)
        z = x+y
        return HttpResponse("<html><body>IM FROM POST METHOD BLOCK <br> Sum is  :"+str(z)+" </body></html>")
        
    
    
    
   