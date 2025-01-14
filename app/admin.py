from django.contrib import admin
from app.models import *
# Register your models here.

class emplyoee_data(admin.ModelAdmin):
    list_display=["eno","ename","esal","eaddr"]


admin.site.register(Employee,emplyoee_data)
