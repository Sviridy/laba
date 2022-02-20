"""Views positions REST"""
import logging
from rest_framework.viewsets import ModelViewSet
from department_app.rest.serializers import PositionsListSerializer
from department_app.models import Positions
logger = logging.getLogger(__name__)
logger.debug('REST_Framework')


class PositionsViewSet(ModelViewSet):
    """"Create, read, update, delete"""
    queryset = Positions.objects.all()
    serializer_class = PositionsListSerializer
