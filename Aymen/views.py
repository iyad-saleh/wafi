from django.shortcuts import render
from company.models import Company
from django.http import HttpResponse
import json

def dashboard(request):
    if hasattr( request.user  ,'is_MANAGER' ) :
        company=''
        try:
            company = Company.objects.filter(name= request.user.company.name).first()
        except Exception as e:
            pass

        return render(request, 'dashboard/admin_home.html',{'company':company})
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "customerListChanged": None,
            })
        })