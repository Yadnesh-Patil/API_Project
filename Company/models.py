from django.db import models

# Create your models here.

# Creating Company Model

class CompanyModel(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    about=models.TextField()
    type_of=models.CharField(max_length=100,choices=(('IT','IT'),
                                                     ('Non IT','Non IT'),
                                                     ('Mobile Phones','Mobile Phones')
                                                     ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name + '--' + self.location

# creating employee model

class EmployeeModel(models.Model):
    name=models.CharField(max_length=100)
    employee_email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=100,choices=(('Manager','Manager'),
                                                      ('Software Developer','Software Developer'),
                                                      ('PL','PL')
                                                      ))
    comp_details=models.ForeignKey(CompanyModel,on_delete=models.CASCADE)