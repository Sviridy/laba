"""Urls"""
from rest_framework.routers import DefaultRouter
from department_app.views import DepartmentViewSet, EmployeeViewSet, PositionsViewSet, SpecializationViewSet

router = DefaultRouter()
router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'positions', PositionsViewSet, basename='positions')
router.register(r'specialization', SpecializationViewSet, basename='specialization')
urlpatterns = router.urls
