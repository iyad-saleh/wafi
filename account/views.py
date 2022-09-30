import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from account.forms import AccountForm
from .models import Account
# from django.contrib.auth.decorators import user_passes_test
# is_MANAGER
# is_RESERVATION
# is_ACCOUNTANT
# is_CUSTOMER
# @user_passes_test(lambda u: u.is_superuser)
def index(request):
    if request.user.is_MANAGER:
        return render(request, 'account/index.html')
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "accountListChanged": None,
            })
        })

# @user_passes_test(lambda u: u.is_superuser)
def account_list(request):
    company = request.user.company
    accounts = Account.objects.filter(company=company)
    return render(request, 'account/account_list.html', {
        'accounts':accounts
    })


# @user_passes_test(lambda u: u.is_superuser)
def edit_account(request, pk):
    account = get_object_or_404(Account, pk=pk)

    # print(account)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        # print(request.POST['account_type'])
        # print(request.POST)
        if form.is_valid():

            account = form.save(commit=False)
            account.company=request.user.company
            account.author=request.user
            # account.account_type=request.POST['account_type']
            account.save()


            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "accountListChanged": None,
                        "showMessage": f"{account.name} updated."
                    })
                }
            )


    else:
        form = AccountForm(instance=account)


    return render(request, 'account/account_form.html', {
        'form': form,

    })

# @user_passes_test(lambda u: u.is_superuser)
@ require_POST
def remove_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    account.soft_delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "accountListChanged": None,
                "showMessage": f"{account.name} deleted."
            })
        })


