from django.shortcuts import render
from company.models import Company
from django.http import HttpResponse
import json
from employee.models import Employee
from customer.models import Customer
from account.models import Account
from django.utils import translation
from django.http import HttpResponseRedirect
from airline.models import FlightSchedule

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
        flightSchedules = FlightSchedule.objects.filter(company=company)
        return render(request, 'dashboard/admin_home.html',
            {
            'company':company,
            'customers':customers,
            'accounts':accounts,
            'employees':employees,
            'flightSchedules':flightSchedules,
            })
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "customerListChanged": None,
            })
        })



def set_language_from_url(request, user_language):
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    # I use HTTP_REFERER to direct them back to previous path
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
