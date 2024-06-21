from django.contrib import admin
from api.models import Employee, Department, Job, Attendence , Payrol
#username : vidya
#password : 123456789
# Register your models here.

class EmployeeAdmin( admin.ModelAdmin):
    list_display=('emp_id', 'first_name','last_name','gender','phone','email')
class DepartmentAdmin( admin.ModelAdmin):
    list_display=('Dept_name','location')
class JobAdmin( admin.ModelAdmin):
    list_display=('Job_title','min_sal','max_sal')
class AttendenceAdmin( admin.ModelAdmin):
    list_display=('employee','date','check_in_time','check_out_time')
class PayrolAdmin( admin.ModelAdmin):
    list_display=('employee','net_salary')


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Attendence,AttendenceAdmin)
admin.site.register(Payrol,PayrolAdmin)

