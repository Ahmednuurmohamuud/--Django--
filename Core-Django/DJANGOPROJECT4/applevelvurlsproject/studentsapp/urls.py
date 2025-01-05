from django.urls import path
from studentsapp import views 


urlpatterns = [
    path('workspace/', views.workspace)
]