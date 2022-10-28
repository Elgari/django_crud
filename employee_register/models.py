from django.db import models


class crud_employee(models.Model):
    employee_name = models.CharField(max_length = 100)
    employee_id = models.IntegerField()
    employee_team = models.CharField(max_length = 100)
    employee_team = models.CharField(max_length = 100)
    employee_teamleader = models.CharField(max_length = 100)
    employee_fulltime = models.CharField(max_length = 1)
    



