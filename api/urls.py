from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
#from rest_framework.routers import DefaultRouter
from api.views import DepartmentViewSet, JobViewSet, EmployeeViewSet, AttendenceViewSet, PayrolViewSet

router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendence', AttendenceViewSet)
router.register(r'payrol', PayrolViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

