from django.shortcuts import render

from rest_framework import viewsets
from api.models import Department, Job, Employee,Attendence, Payrol
from api.serializers import DepartmentSerializer, JobSerializer, EmployeeSerializer, AttendenceSerializer , PayrolSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
   
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    # urls will be  = empolyee/{emp_id}/attendence
    @action(detail=True,methods=['get'])
    def attendence(self,request,pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
            attend = Attendence.objects.filter(employee=employee)
            emp_serializer = AttendenceSerializer(attend,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'Employee doesnot exist '})
     # urls will be  = empolyee/{emp_id}/payrol
    @action(detail=True,methods=['get'])
    def payrol(self,request,pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
            pay= Payrol.objects.filter(employee=employee)
            pay_serializer = PayrolSerializer(pay,many=True,context={'request':request})
            return Response(pay_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'Employee doesnot exist '})



class AttendenceViewSet(viewsets.ModelViewSet):
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer

class PayrolViewSet(viewsets.ModelViewSet):
    queryset = Payrol.objects.all()
    serializer_class = PayrolSerializer

