"""Views"""
import logging
logger = logging.getLogger(__name__)
logger.debug('REST_Framework')
from department_app.views.department_views import DepartmentCreateView, DepartmentListView, DepartmentDetailView
from department_app.views.employee_views import EmployeeCreateView, EmployeeListView, EmployeeDetailView
from department_app.views.specialization_views import SpecializationCreateView, SpecializationListView, \
    SpecializationDetailView
from department_app.views.positions_views import PositionsCreateView, PositionsListView, PositionsDetailView
