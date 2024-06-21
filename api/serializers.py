from rest_framework import serializers
from api.models import Department, Job, Employee, Attendence, Payrol

#create serializer here 
class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    dept_id=serializers.ReadOnlyField()
    class Meta:
        model = Department
        fields = '__all__'

class JobSerializer(serializers.HyperlinkedModelSerializer):
    job_id=serializers.ReadOnlyField()
    class Meta:
        model = Job
        fields = '__all__'

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    emp_id=serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'

class AttendenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendence 
        fields = '__all__'

class PayrolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payrol 
        fields = '__all__'

