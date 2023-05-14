from django.contrib import admin
from .models import CompanyModel, EmployeeModel

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=['name','location','type_of']
    search_fields=['name',]

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','employee_email','comp_details']
    list_filter=['comp_details',]

admin.site.register(CompanyModel,CompanyAdmin)

admin.site.register(EmployeeModel,EmployeeAdmin)
