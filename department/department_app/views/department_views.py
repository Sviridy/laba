"""Views department"""
from department_app.rest.serializers import DepartmentListSerializer
from department_app.models import Department
from rest_framework import viewsets


class DepartmentViewSet(viewsets.ModelViewSet):
    """Create, read, update, delete"""
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer


# class DepartmentHome(ListView):
#     model = Department
#     template_name = 'department.html'
#     context_object_name = 'department'
#
#
# class EditDepartment(UpdateView):
#     model = Department
#     fields = ['department']
#     template_name = 'edit_department.html'
#     pk_url_kwarg = 'department_id'
#     context_object_name = 'department'
#     success_url = reverse_lazy('department')
#
#
# class AddDepartment(CreateView):
#     model = Department
#     fields = ['department']
#     template_name = 'add_department.html'
#     context_object_name = 'department'
#     success_url = reverse_lazy('department')
#
#
# def delete_department(request, department_id):
#     Department.objects.get(id=department_id).delete()
#     return HttpResponseRedirect("/department/")
