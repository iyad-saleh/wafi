import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Passport, Passenger, Photo
from .forms import PassportForm, PassengerForm, PhotoForm
from django.contrib.auth.decorators import user_passes_test
# is_MANAGER
# is_RESERVATION
# is_ACCOUNTANT
# is_CUSTOMER
@login_required
def index(request):
    form = PassportForm()
    passports = Passport.objects.all().order_by('-id')
    if request.user.is_MANAGER or request.user.is_RESERVATION or request.user.is_CUSTOMER:
        return render(request, 'passport/index.html',{'form':form, 'passports':passports})


@login_required
def passport_list(request):
    if request.user.is_MANAGER or request.user.is_RESERVATION or request.user.is_CUSTOMER:
        passports = Passport.objects.all().order_by('-id')
        return render(request, 'passport/passport_list.html', {
            'passports':passports
        })


@login_required
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
        if form.is_valid() :
            passport = form.save(commit=False)
            passport.author=request.user
            passport.company=request.user.company

            passport.save()
            images = request.FILES.getlist('images')
            for image in images:
                photo = Photo.objects.create(
                    passport=passport,
                    image=image,
                )

            # print(category)
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "passportListChanged": None,
                        "showMessage": f"passport {passport} added."
                    })
                })
        else:
            return render(request, 'passport/passport_form.html', {
        'form': form
    })
    else:
        form = PassportForm()
    return render(request, 'passport/passport_form.html', {
        'form': form
    })

@login_required
def edit_passport(request, pk):
    passport = get_object_or_404(Passport, pk=pk)
    images = get_object_or_404(Photo , pk = passport.account.pk)
    if request.method == "POST":
        form = PassportForm(request.POST,request.FILES, instance=passport)
        photoform = PassportForm(request.POST, instance=account)
        # print(request.FILES, 'form.is_valid')

        if form.is_valid()and accountForm.is_valid():
            account = accountForm.save(commit=False)
            account.company=request.user.company
            account.author=request.user
            account.account_type='20'
            account.save()
            # print("form",form )
            passport = form.save(commit=False)
            passport.author=request.user
            passport.company=request.user.company
            passport.account=account

            passport.save()


            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "passportListChanged": None,
                        "showMessage": f"{passport.account.name} updated."
                    })
                }
            )
    else:
        form = PassportForm(instance=passport)
        accountForm = AccountForm(instance=account)
        # print('form   :  ',form)
    return render(request, 'passport/passport_form.html', {
        'form': form,'accountForm':accountForm,
        'passport': passport,
    })

@login_required
@ require_POST
def remove_passport(request, pk):
    passport = get_object_or_404(Passport, pk=pk)
    account = get_object_or_404(Account , pk = passport.account.pk)
    account.soft_delete()
    passport.soft_delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "passportListChanged": None,
                "showMessage": f"{passport.account.name} deleted."
            })
        })


