import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Passport
from .forms import PassportForm
from django.contrib.auth.decorators import user_passes_test
# is_MANAGER
# is_RESERVATION
# is_ACCOUNTANT
# is_CUSTOMER
# @user_passes_test(lambda u: u.is_MANAGER)
def index(request):
    form = PassportForm()
    if request.user.is_MANAGER or request.user.is_RESERVATION or request.user.is_CUSTOMER:
        return render(request, 'passport/index_Type.html',{'form':form})


# @user_passes_test(lambda u: u.is_MANAGER)
def passport_list(request):
    if request.user.is_MANAGER or request.user.is_RESERVATION or request.user.is_CUSTOMER:
        passports = Passport.objects.all()
        return render(request, 'passport/passport_list.html', {
            'passports':passports
        })

# @user_passes_test(lambda u: u.is_superuser)
def add_passport(request):
    if not request.user.is_MANAGER:
        return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "passportListChanged": None,
            })
        })
    if request.method == "POST":

        form = PassportForm(request.POST)
        # print("request.POST: ",request.POST)
        if form.is_valid() :

            passport = form.save(commit=False)
            passport.author=request.user
            passport.save()

            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "passportListChanged": None,
                        "showMessage": f"{passport} added."
                    })
                })
        else:
            return render(request, 'passport/TypeForm.html', {
        'form': form
    })
    else:

        form = PassportForm()
    return render(request, 'passport/TypeForm.html', {
        'form': form
    })

# @user_passes_test(lambda u: u.is_superuser)
def edit_passport(request, pk):
    passport = get_object_or_404(Passport, pk=pk)

    if request.method == "POST":
        form = PassportForm(request.POST, instance=passport)

        if form.is_valid():

            passport = form.save(commit=False)
            passport.author=request.user
            passport.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "passportListChanged": None,
                        "showMessage": f"{passport} updated."
                    })
                }
            )
    else:
        form = PassportForm(instance=passport)

    return render(request, 'passport/passport_form.html', {
        'form': form,'passport': passport,
    })

# @user_passes_test(lambda u: u.is_superuser)
@ require_POST
def remove_passport(request, pk):
    passport = get_object_or_404(Passport, pk=pk)
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "passportListChanged": None,
                "showMessage": f"{passport} deleted."
            })
        })


