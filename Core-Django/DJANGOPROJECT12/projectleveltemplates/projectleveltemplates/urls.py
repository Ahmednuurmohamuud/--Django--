"""
URL configuration for projectleveltemplates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="homeurlname"),
    path('', views.starbucks_view, name="home"),
    path('tourism/',views.tourism, name="tourismurlname"),
    path('beach/', views.beach, name="beachurlname"),
    path('children/', views.children, name="childrenurlname"),
    path('programmerspage/', views.programmerspage, name="programmerspage"),
    path('adddata/', views.adding_bulkdata_view, name="adddata"),

    path('somalia_data/', views.somalia_data, name="somalia_data"),
    path('mogadisu_data/', views.mogadisu_data, name="mogadisu_data"),
    path('hyderabad_data/', views.hyderabad_data, name="hyderabad_data"),
    path('mubai_data/', views.mumbai_data, name="mubai_data"),
]


