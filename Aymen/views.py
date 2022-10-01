from django.shortcuts import render
from company.models import Company
from django.http import HttpResponse
import json
from employee.models import Employee
from customer.models import Customer
from account.models import Account



def dashboard(request):
    if hasattr( request.user  ,'is_MANAGER' ) :
        company=''
        try:
            company = Company.objects.filter(name= request.user.company.name).first()
        except Exception as e:
            pass
        company = request.user.company
        customers = Customer.objects.filter(company=company)
        accounts = Account.objects.filter(company=company)
        employees = Employee.objects.filter(company=company)
        return render(request, 'dashboard/admin_home.html',
            {
            'company':company,
            'customers':customers,
            'accounts':accounts,
            'employees':employees,
            })
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "customerListChanged": None,
            })
        })