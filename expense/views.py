import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Expense
from .forms import ExpenseForm
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
    return render(request, 'expense/index.html',{'accountForm':form})
    # return HttpResponse(
    #     status=403,
    #     headers={
    #         'HX-Trigger': json.dumps({

    #            "expenseListChanged": None,
    #         })
    #     })

@user_passes_test(lambda u: u.is_MANAGER)
def expense_list(request):
    company = request.user.company
    expenses = Expense.objects.filter(company=company)
    return render(request, 'expense/expense_list.html', {
        'expenses':expenses
    })

@user_passes_test(lambda u: u.is_MANAGER)
def add_expense(request):
    if not request.user.is_MANAGER:
        return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "expenseListChanged": None,
            })
        })
    if request.method == "POST":
        accountForm = AccountForm(request.POST)
        form = ExpenseForm(request.POST)
        # print("request.POST: ",request.POST)
        if form.is_valid() and accountForm.is_valid():
            # print('form is valid ')
            try:
                account = accountForm.save(commit=False)
                account.company=request.user.company
                account.author=request.user
                account.account_type= '16'
                account.save()

                expense = form.save(commit=False)
                expense.author=request.user
                expense.company=request.user.company
                expense.account=account

                expense.save()
            except Exception as e:
                return HttpResponse(
                status=500,
                headers={
                    'HX-Trigger': json.dumps({
                        "expenseListChanged": None,
                        "showMessage": f"{account.name} {e}."
                    })
                })




            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "expenseListChanged": None,
                        "showMessage": f"{expense.account.name} added."
                    })
                })


    else:
        accountForm = AccountForm()
        form = ExpenseForm()
    return render(request, 'expense/expense_form.html', {
        'form': form,'accountForm':accountForm
    })

@user_passes_test(lambda u: u.is_MANAGER)
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    account = get_object_or_404(Account , pk = expense.account.pk)
    # print(account)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        accountForm = AccountForm(request.POST, instance=account)
        if form.is_valid()and accountForm.is_valid():
            try:

                account = accountForm.save(commit=False)
                account.company=request.user.company
                account.author=request.user
                account.account_type= '16'
                account.save()

                expense = form.save(commit=False)
                expense.author=request.user
                expense.company=request.user.company
                expense.account=account

                expense.save()
            except Exception as e:
                return HttpResponse(
                status=500,
                headers={
                    'HX-Trigger': json.dumps({
                        "expenseListChanged": None,
                        "showMessage": f"{account.name} {e}."
                    })
                })

            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "expenseListChanged": None,
                        "showMessage": f"{expense.account.name} updated."
                    })
                }
            )
    else:
        form = ExpenseForm(instance=expense)
        accountForm = AccountForm(instance=account)
    return render(request, 'expense/expense_form.html', {
        'form': form,'accountForm':accountForm,
        'expense': expense,
    })

@user_passes_test(lambda u: u.is_MANAGER)
@ require_POST
def remove_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    account = get_object_or_404(Account , pk = expense.account.pk)
    account.soft_delete()
    expense.soft_delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "expenseListChanged": None,
                "showMessage": f"{expense.account.name} deleted."
            })
        })


