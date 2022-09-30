import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Employee, EmployeeType
from .forms import EmployeeForm , Employee_TypeForm
from account.forms import AccountForm
from account.models import Account
from django.contrib.auth.decorators import user_passes_test
# is_MANAGER
# is_RESERVATION
# is_ACCOUNTANT
# is_CUSTOMER
@user_passes_test(lambda u: u.is_MANAGER)
def index(request):
    # if request.user.is_MANAGER:
    return render(request, 'employee/index.html')
    # return HttpResponse(
    #     status=403,
    #     headers={
    #         'HX-Trigger': json.dumps({

    #            "employeeListChanged": None,
    #         })
    #     })

@user_passes_test(lambda u: u.is_MANAGER)
def employee_list(request):
    company = request.user.company
    emps = Employee.objects.filter(company=company)
    return render(request, 'employee/employee_list.html', {
        'employees':emps
    })

# @user_passes_test(lambda u: u.is_superuser)
def add_employee(request):
    if not request.user.is_MANAGER:
        return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "employeeListChanged": None,
            })
        })
    if request.method == "POST":
        accountForm = AccountForm(request.POST)
        form = EmployeeForm(request.POST)
        # print("request.POST: ",request.POST)
        if form.is_valid() and accountForm.is_valid():
            # print('form is valid ')
            account = accountForm.save(commit=False)
            account.company=request.user.company
            account.author=request.user
            account.account_type= '31'
            account.save()

            employee = form.save(commit=False)
            employee.author=request.user
            employee.company=request.user.company
            employee.account=account

            employee.save()

            cats =form.cleaned_data['category']
            for cat in cats:
                employee.category.add(cat)
            # print(category)
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "employeeListChanged": None,
                        "showMessage": f"{employee.account.name} added."
                    })
                })
        else:
            return render(request, 'employee/employee_form.html', {
        'form': form,'accountForm':accountForm
    })
    else:
        accountForm = AccountForm()
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {
        'form': form,'accountForm':accountForm
    })

# @user_passes_test(lambda u: u.is_superuser)
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    account = get_object_or_404(Account , pk = employee.account.pk)
    # print(account)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        accountForm = AccountForm(request.POST, instance=account)
        if form.is_valid()and accountForm.is_valid():

            account = accountForm.save(commit=False)
            account.company=request.user.company
            account.author=request.user
            account.save()

            employee = form.save(commit=False)
            employee.author=request.user
            employee.company=request.user.company
            employee.account=account

            employee.save()
            employee.category.clear()
            cats =form.cleaned_data['category']
            for cat in cats:
                employee.category.add(cat)

            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "employeeListChanged": None,
                        "showMessage": f"{employee.account.name} updated."
                    })
                }
            )
    else:
        form = EmployeeForm(instance=employee)
        accountForm = AccountForm(instance=account)
    return render(request, 'employee/employee_form.html', {
        'form': form,'accountForm':accountForm,
        'employee': employee,
    })

# @user_passes_test(lambda u: u.is_superuser)
@ require_POST
def remove_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    account = get_object_or_404(Account , pk = employee.account.pk)
    account.soft_delete()
    employee.soft_delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "employeeListChanged": None,
                "showMessage": f"{employee.account.name} deleted."
            })
        })


def indexType(request):
    if request.user.is_MANAGER:
        form = Employee_TypeForm()
        return render(request, 'employee/index_Type.html',{'form': form})
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "employeeTypeListChanged": None,
            })
        })

# @user_passes_test(lambda u: u.is_superuser)
def employee_Type_list(request):
    company = request.user.company

    empTypes = EmployeeType.objects.filter(company=company)
    return render(request, 'employee/employee_Type_list.html', {
        'empTypes':empTypes
    })

# @user_passes_test(lambda u: u.is_superuser)
def add_employee_Type(request):
    if request.method == "POST":
        form = Employee_TypeForm(request.POST)
        if form.is_valid():
            employee_type = form.save(commit=False)
            employee_type.author=request.user
            employee_type.company=request.user.company
            print('request.user.company',request.user.company)
            employee_type.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "employeeTypeListChanged": None,
                        "showMessage": f"{employee_type.category} added."
                    })
                })
    else:
        form = Employee_TypeForm()
    return render(request, 'employee/employee_Type_form.html', {
        'form': form,
    })

# @user_passes_test(lambda u: u.is_superuser)
def edit_employee_Type(request, pk):
    employeeType = get_object_or_404(EmployeeType, pk=pk)
    if request.method == "POST":
        form = Employee_TypeForm(request.POST, instance=employeeType)
        if form.is_valid():
            employeeType = form.save(commit=False)
            employeeType.author=request.user

            employeeType.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "employeeTypeListChanged": None,
                        "showMessage": f"{employeeType.category} updated."
                    })
                }
            )
    else:
        form = Employee_TypeForm(instance=employeeType)
    return render(request, 'employee/employee_Type_form.html', {
        'form': form,
        'employeeType': employeeType,
    })

# @user_passes_test(lambda u: u.is_superuser)
@ require_POST
def remove_employee_Type(request, pk):
    employeeType = get_object_or_404(EmployeeType, pk=pk)
    employeeType.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "employeeTypeListChanged": None,
                "showMessage": f"{employeeType.category} deleted."
            })
        })
