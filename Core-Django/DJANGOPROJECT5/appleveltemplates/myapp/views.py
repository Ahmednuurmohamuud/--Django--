from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'myapp/home.html')

def contact_view(request):
    return render(request, 'myapp/contact.html')

def about_view(request):
    return render(request, 'myapp/about.html')
