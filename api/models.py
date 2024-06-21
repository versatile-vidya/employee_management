from django.db import models

# Create your models here.from django.db import models

class Department(models.Model):
    Dept_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.Dept_name

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    Job_title = models.CharField(max_length=100)
    min_sal = models.DecimalField(max_digits=10, decimal_places=2)
    max_sal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Job_title

class Employee(models.Model):
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female'),('O', 'Other'),]
    
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M') 
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendence(models.Model):
    at_id = models.AutoField(primary_key=True)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time =  models.TimeField()
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    def __str__(self):
        return self.date

class Payrol(models.Model):
    pay_id = models.AutoField(primary_key=True)
    pay_date = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.net_salary  
