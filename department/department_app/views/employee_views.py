"""Views employee REST"""
from rest_framework.viewsets import ModelViewSet
from department_app.rest.serializers import EmployeeListSerializer
from department_app.models import Employee


class EmployeeViewSet(ModelViewSet):
    """"Create, read, update, delete"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer
