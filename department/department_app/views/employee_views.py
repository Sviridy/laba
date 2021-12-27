"""Views employee"""
from department_app.rest.serializers import EmployeeListSerializer
from department_app.models import Employee
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    """"Create, read, update, delete"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer


# class EmployeeHome(ListView):
#     model = Employee
#     template_name = 'employee.html'
#     context_object_name = 'employee'
#
#
# class EmployeeSearch(ListView):
#     model = Employee
#     template_name = 'employee_search.html'
#     context_object_name = 'employee'
#
#     def get_queryset(self):
#         query1 = self.request.GET.get('date1')
#         query2 = self.request.GET.get('date2')
#         employee = Employee.objects.filter(date_of_birth__range=[query1, query2])
#         return employee
#
#
# class EditEmployee(UpdateView):
#     model = Employee
#     fields = ['name', 'date_of_birth', 'department', 'positions', 'specialization', 'experience', 'wages']
#     template_name = 'edit_employee.html'
#     pk_url_kwarg = 'employee_id'
#     context_object_name = 'employee'
#     success_url = reverse_lazy('employee')
#
#     def get_form(self, form_class=None):
#         form = super(EditEmployee, self).get_form(form_class)
#         form.fields['department'].empty_label = 'Department not selected'
#         form.fields['positions'].empty_label = 'Positions not selected'
#         form.fields['specialization'].empty_label = 'Specialization not selected'
#         return form
#
#
# class AddEmployee(CreateView):
#     model = Employee
#     fields = ['name', 'date_of_birth', 'department', 'positions', 'specialization', 'experience', 'wages']
#     template_name = 'add_employee.html'
#     context_object_name = 'employee'
#     success_url = reverse_lazy('employee')
#
#     def get_form(self, form_class=None):
#         form = super(AddEmployee, self).get_form(form_class)
#         # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
#         form.fields['department'].empty_label = 'Department not selected'
#         form.fields['positions'].empty_label = 'Positions not selected'
#         form.fields['specialization'].empty_label = 'Specialization not selected'
#         return form
#
#
# def delete_employee(request, employee_id):
#     Employee.objects.get(id=employee_id).delete()
#     return HttpResponseRedirect("/employee/")
