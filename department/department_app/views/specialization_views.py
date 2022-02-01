"""Views specialization REST"""
from rest_framework.viewsets import ModelViewSet
from department_app.rest.serializers import SpecializationListSerializer
from department_app.models import Specialization


class SpecializationViewSet(ModelViewSet):
    """"Create, read, update, delete"""
    queryset = Specialization.objects.all()
    serializer_class = SpecializationListSerializer
