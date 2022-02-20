"""Views specialization REST"""
import logging
from rest_framework.viewsets import ModelViewSet
from department_app.rest.serializers import SpecializationListSerializer
from department_app.models import Specialization
logger = logging.getLogger(__name__)
logger.debug('REST_Framework')


class SpecializationViewSet(ModelViewSet):
    """"Create, read, update, delete"""
    queryset = Specialization.objects.all()
    serializer_class = SpecializationListSerializer
