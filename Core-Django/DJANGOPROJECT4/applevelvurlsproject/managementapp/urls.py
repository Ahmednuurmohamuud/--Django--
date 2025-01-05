from django.urls import path

from managementapp import views

urlpatterns = [
    path('adminconsole/', views.adminconsole),
    path('adminemployees/', views.adminemps),
]