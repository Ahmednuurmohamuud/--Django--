from django.contrib import admin
from myapp.models import Employee, Student, Management, Company, Programmer

# Register your models here.

admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Management)
admin.site.register(Company)
admin.site.register(Programmer)