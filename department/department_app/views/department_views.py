"""Views department REST"""
import logging
from rest_framework.viewsets import ModelViewSet
from department_app.rest.serializers import DepartmentListSerializer
from department_app.models import Department
logger = logging.getLogger(__name__)
logger.debug('REST_Framework')


class DepartmentViewSet(ModelViewSet):
    """Create, read, update, delete"""
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer
