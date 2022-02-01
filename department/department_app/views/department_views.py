"""Views department REST"""
from rest_framework.viewsets import ModelViewSet
from department_app.rest.serializers import DepartmentListSerializer
from department_app.models import Department


class DepartmentViewSet(ModelViewSet):
    """Create, read, update, delete"""
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer
