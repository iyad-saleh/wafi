import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Passport, Passenger, Photo
from .forms import PassportForm, PassengerForm, PhotoFormSet
from django.contrib.auth.decorators import user_passes_test
# is_MANAGER
# is_RESERVATION
# is_ACCOUNTANT
# is_CUSTOMER
@login_required
def index(request):
    form = PassportForm()
    photoform =PhotoFormSet()
    passports = Passport.objects.all().order_by('-id')
    if request.user.is_MANAGER or request.user.is_RESERVATION or request.user.is_CUSTOMER:
        return render(request, 'passport/index.html',{'form':form,'photoform':photoform ,'passports':passports})


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
        photoform= PhotoFormSet(request.POST,request.FILES)
        if form.is_valid()and photoform.is_valid() :
            passport = form.save(commit=False)
            passport.author=request.user
            passport.company=request.user.company

            passport.save()
            # images = request.FILES.getlist('images')
            # for image in images:
            #     photo = Photo.objects.create(
            #         passport=passport,
            #         image=image,
            #     )
            photos = photoform.save(commit=False)
            for photo in photos:
                photo.passport=passport
                # print(photos)
                photo.save()
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
        'form': form,'photoform':photoform
    })
    else:
        form = PassportForm()
        photoform= PhotoFormSet()
    return render(request, 'passport/passport_form.html', {
        'form': form,'photoform':photoform
    })

@login_required
def edit_passport(request, pk):
    passport = get_object_or_404(Passport, pk=pk)
    images = get_object_or_404(Photo , pk = passport.pk)
    if request.method == "POST":
        form = PassportForm(request.POST, instance=passport)
        photoform = PhotoFormSet(request.POST,request.FILES)
        # print(request.FILES, 'form.is_valid')

        if form.is_valid()and photoform.is_valid():
            passport = form.save(commit=False)
            passport.author=request.user
            passport.company=request.user.company
            passport.save()
            photos = photoform.save(commit=False)
            for photo in photos:
                photo.passport=passport
                # print(photos)
                photo.save()

            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "passportListChanged": None,
                        "showMessage": f"passport :{passport} updated."
                    })
                }
            )
    else:
        form = PassportForm(instance=passport)
        accountForm = PhotoFormSet(instance=account)
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


