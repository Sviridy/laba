"""Views employee REST"""
import logging
from rest_framework.viewsets import ModelViewSet
from department_app.rest.serializers import EmployeeListSerializer
from department_app.models import Employee
logger = logging.getLogger(__name__)
logger.debug('REST_Framework')


class EmployeeViewSet(ModelViewSet):
    """"Create, read, update, delete"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer
