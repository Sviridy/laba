"""Urls"""
from django.urls import path
from department_app.views import DepartmentViewSet, EmployeeViewSet, PositionsViewSet, SpecializationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'positions', PositionsViewSet, basename='positions')
router.register(r'specialization', SpecializationViewSet, basename='specialization')
urlpatterns = router.urls

# urlpatterns = [
#     path('department/create/', DepartmentCreateView.as_view()),
#     path('department/all/', DepartmentListView.as_view()),
#     path('department/detail/<int:pk>/', DepartmentDetailView.as_view()),
#     path('employee/create/', EmployeeCreateView.as_view()),
#     path('employee/all/', EmployeeListView.as_view()),
#     path('employee/detail/<int:pk>/', EmployeeDetailView.as_view()),
#     path('positions/create/', PositionsCreateView.as_view()),
#     path('positions/all/', PositionsListView.as_view()),
#     path('positions/detail/<int:pk>/', PositionsDetailView.as_view()),
#     path('specialization/create/', SpecializationCreateView.as_view()),
#     path('specialization/all/', SpecializationListView.as_view()),
#     path('specialization/detail/<int:pk>/', SpecializationDetailView.as_view()),
# ]
