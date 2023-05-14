from rest_framework import serializers
from .models import CompanyModel , EmployeeModel
#create serializers here

# creating Company model serializer
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=CompanyModel
        fields="__all__"

# creating Employee model serializer
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=EmployeeModel
        fields="__all__"