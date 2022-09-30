import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Box
from .forms import BoxForm
from account.forms import AccountForm
from account.models import Account
from django.contrib.auth.decorators import user_passes_test
# is_MANAGER
# is_RESERVATION
# is_ACCOUNTANT
# is_CUSTOMER
@user_passes_test(lambda u: u.is_MANAGER)
def index(request):
    form = AccountForm()
    return render(request, 'box/index.html',{'accountForm':form})
    # return HttpResponse(
    #     status=403,
    #     headers={
    #         'HX-Trigger': json.dumps({

    #            "boxListChanged": None,
    #         })
    #     })

@user_passes_test(lambda u: u.is_MANAGER)
def box_list(request):
    company = request.user.company
    boxs = Box.objects.filter(company=company)
    return render(request, 'box/box_list.html', {
        'boxs':boxs
    })

@user_passes_test(lambda u: u.is_MANAGER)
def add_box(request):
    if not request.user.is_MANAGER:
        return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "boxListChanged": None,
            })
        })
    if request.method == "POST":
        accountForm = AccountForm(request.POST)
        form = BoxForm(request.POST)
        # print("request.POST: ",request.POST)
        if form.is_valid() and accountForm.is_valid():
            # print('form is valid ')
            try:
                account = accountForm.save(commit=False)
                account.company=request.user.company
                account.author=request.user
                account.account_type= '32'
                account.save()

                box = form.save(commit=False)
                box.author=request.user
                box.company=request.user.company
                box.account=account

                box.save()
            except Exception as e:
                return HttpResponse(
                status=500,
                headers={
                    'HX-Trigger': json.dumps({
                        "boxListChanged": None,
                        "showMessage": f"{account.name} {e}."
                    })
                })




            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "boxListChanged": None,
                        "showMessage": f"{box.account.name} added."
                    })
                })


    else:
        accountForm = AccountForm()
        form = BoxForm()
    return render(request, 'box/box_form.html', {
        'form': form,'accountForm':accountForm
    })

@user_passes_test(lambda u: u.is_MANAGER)
def edit_box(request, pk):
    box = get_object_or_404(Box, pk=pk)
    account = get_object_or_404(Account , pk = box.account.pk)
    # print(account)
    if request.method == "POST":
        form = BoxForm(request.POST, instance=box)
        accountForm = AccountForm(request.POST, instance=account)
        if form.is_valid()and accountForm.is_valid():
            try:

                account = accountForm.save(commit=False)
                account.company=request.user.company
                account.author=request.user
                account.account_type= '16'
                account.save()

                box = form.save(commit=False)
                box.author=request.user
                box.company=request.user.company
                box.account=account

                box.save()
            except Exception as e:
                return HttpResponse(
                status=500,
                headers={
                    'HX-Trigger': json.dumps({
                        "boxListChanged": None,
                        "showMessage": f"{account.name} {e}."
                    })
                })

            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "boxListChanged": None,
                        "showMessage": f"{box.account.name} updated."
                    })
                }
            )
    else:
        form = BoxForm(instance=box)
        accountForm = AccountForm(instance=account)
    return render(request, 'box/box_form.html', {
        'form': form,'accountForm':accountForm,
        'box': box,
    })

@user_passes_test(lambda u: u.is_MANAGER)
@ require_POST
def remove_box(request, pk):
    box = get_object_or_404(Box, pk=pk)
    account = get_object_or_404(Account , pk = box.account.pk)
    account.soft_delete()
    box.soft_delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "boxListChanged": None,
                "showMessage": f"{box.account.name} deleted."
            })
        })


