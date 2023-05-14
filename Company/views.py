from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from rest_framework import viewsets
from .models import CompanyModel , EmployeeModel
from .serializers import CompanySerializer , EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

def home(request):
    print('Home Page Requested')
    l=['ankit','ravi','uttam']
    # return JsonResponse(l,safe=False)
    return HttpResponse('<h1>This Home Page is requested</h1>')

class CompanyViewset(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()  #fetching all data from the Company Model
    serializer_class=CompanySerializer



    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):

        try:
            company = CompanyModel.objects.get(company_id=pk)
            emps = EmployeeModel.objects.filter(comp_details=company)
            emp_serializer = EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            return Response({
                'Message':'Company does not exist'
            })
            


class EmployeeViewset(viewsets.ModelViewSet):
    queryset=EmployeeModel.objects.all()   #fetching all data from the Employee Model
    serializer_class=EmployeeSerializer