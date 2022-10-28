from django.shortcuts import render
from employee_register.models import crud_employee
from django.contrib import messages

def employee_display(request):
    results = crud_employee.objects.all()
    return render(request, "Index.html", {"crud_employee":results})

def employee_insert(request):
    if request.method == "POST":
        if request.POST.get('employee_name') and request.POST.get('employee_id') and request.POST.get('employee_team') and request.POST.get('employee_team_employees') and request.POST.get('employee_teamleader') and request.POST.get('employee_fulltime'):
            save_emp = crud_employee()
            save_emp.employee_name = request.POST.get('employee_name')
            save_emp.employee_id = request.POST.get('employee_id')
            save_emp.employee_team = request.POST.get('employee_team')
            save_emp.employee_team_employees = request.POST.get('employee_team_employees')
            save_emp.employee_teamleader = request.POST.get('employee_teamleader')
            save_emp.employee_team = request.POST.get('employee_fulltime')
            save_emp.save()
            
        messages.success(request , "The record is saved succesfully!")
        return render(request, "Create.html")
        
    return render(request, "Create.html")


            

