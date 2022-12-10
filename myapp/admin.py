from django.contrib import admin
from myapp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'address']
admin.site.register(Student, StudentAdmin)