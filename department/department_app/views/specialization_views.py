"""Views specialization"""
from department_app.rest.serializers import SpecializationListSerializer
from department_app.models import Specialization
from rest_framework import viewsets


class SpecializationViewSet(viewsets.ModelViewSet):
    """"Create, read, update, delete"""
    queryset = Specialization.objects.all()
    serializer_class = SpecializationListSerializer


# class SpecializationHome(ListView):
#     model = Specialization
#     template_name = 'specialization.html'
#     context_object_name = 'specialization'
#
#
# class EditSpecialization(UpdateView):
#     model = Specialization
#     fields = ['name']
#     template_name = 'edit_specialization.html'
#     pk_url_kwarg = 'specialization_id'
#     context_object_name = 'specialization'
#     success_url = reverse_lazy('specialization')
#
#
# class AddSpecialization(CreateView):
#     model = Specialization
#     fields = ['name']
#     template_name = 'add_specialization.html'
#     context_object_name = 'specialization'
#     success_url = reverse_lazy('specialization')
#
#
# def delete_specialization(request, specialization_id):
#     Specialization.objects.get(id=specialization_id).delete()
#     return HttpResponseRedirect("/specialization/")
