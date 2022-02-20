"""Views"""
from department_app.views.department_views import DepartmentViewSet
from department_app.views.department_app_views import DepartmentHome, AddDepartment, EditDepartment, delete_department
from department_app.views.employee_views import EmployeeViewSet
from department_app.views.employee_app_views import EmployeeHome, AddEmployee, EditEmployee, delete_employee, \
    EmployeeSearch
from department_app.views.specialization_views import SpecializationViewSet
from department_app.views.specialization_app_views import SpecializationHome, EditSpecialization, AddSpecialization, \
    delete_specialization
from department_app.views.positions_views import PositionsViewSet
from department_app.views.positions_app_views import PositionsHome, EditPositions, AddPositions, delete
