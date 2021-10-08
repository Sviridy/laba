"""Views employee"""
from rest_framework import generics
from department_app.rest.serializers import EmployeeListSerializer
from department_app.models import Employee


class EmployeeCreateView(generics.CreateAPIView):
    """Create employee"""
    serializer_class = EmployeeListSerializer


class EmployeeListView(generics.ListAPIView):
    """Read all employee"""
    serializer_class = EmployeeListSerializer
    queryset = Employee.objects.all()


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Read, update, delete"""
    serializer_class = EmployeeListSerializer
    queryset = Employee.objects.all()
