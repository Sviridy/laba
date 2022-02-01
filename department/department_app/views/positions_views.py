"""Views positions REST"""
from rest_framework.viewsets import ModelViewSet
from department_app.rest.serializers import PositionsListSerializer
from department_app.models import Positions


class PositionsViewSet(ModelViewSet):
    """"Create, read, update, delete"""
    queryset = Positions.objects.all()
    serializer_class = PositionsListSerializer
