from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def account_index(request):
    if request.user.is_MANAGER:
        return render(request, 'account/index.html')
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "accountListChanged": None,
            })
        })