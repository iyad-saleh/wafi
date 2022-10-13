import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Passport, Passenger, Photo
from .forms import PassportForm, PassengerForm, PhotoFormSet
from django.contrib.auth.decorators import user_passes_test

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models import Q # new
# is_MANAGER
# is_RESERVATION
# is_ACCOUNTANT
# is_CUSTOMER
@login_required
def index(request):
    form = PassportForm()
    photoform =PhotoFormSet()
    passport_list = Passport.objects.all().order_by('-id')
    paginator = Paginator(passport_list, 5)
    page = request.GET.get('page', 1)
    try:
        passports = paginator.page(page)
    except PageNotAnInteger:
        passports = paginator.page(1)
    except EmptyPage:
        passports = paginator.page(paginator.num_pages)

    if request.user.is_MANAGER or request.user.is_RESERVATION or request.user.is_CUSTOMER:
        return render(request, 'passport/index.html',
            {'form':form,
            'photoform':photoform ,
            'passports':passports,
            'page': page})



@login_required
def searchPassport(request):
    search_text = request.GET.get('search')
    passport_list = Passport.objects.filter(Q(first_name__icontains=search_text)
                                    |Q(last_name__icontains=search_text)
                                    |Q(passport_number__icontains=search_text)).distinct()
    paginator = Paginator(passport_list, 5)
    page = request.GET.get('page', 1)
    try:
        passports = paginator.page(page)
    except PageNotAnInteger:
        passports = paginator.page(1)
    except EmptyPage:
        passports = paginator.page(paginator.num_pages)

    return render(request, 'passport/passportlist.html', {
        'passports':passports, 'page': page
    })

@login_required
def PassportList(request):
    if request.user.is_MANAGER or request.user.is_RESERVATION or request.user.is_CUSTOMER:

        passport_list = Passport.objects.all().order_by('-id')
        paginator = Paginator(passport_list, 5)
        page = request.GET.get('page', 1)
        try:
            passports = paginator.page(page)
        except PageNotAnInteger:
            passports = paginator.page(1)
        except EmptyPage:
            passports = paginator.page(paginator.num_pages)

        return render(request, 'passport/passportlist.html', {
            'passports':passports, 'page': page
        })


@login_required
def passport_list(request):
    if request.user.is_MANAGER or request.user.is_RESERVATION or request.user.is_CUSTOMER:

        passport_list = Passport.objects.all().order_by('-id')
        paginator = Paginator(passport_list, 5)
        page = request.GET.get('page', 1)
        try:
            passports = paginator.page(page)
        except PageNotAnInteger:
            passports = paginator.page(1)
        except EmptyPage:
            passports = paginator.page(paginator.num_pages)

        return render(request, 'passport/passport_list.html', {
            'passports':passports, 'page': page
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
        form = PassportForm(request.POST,request.FILES)
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
    if passport :
        images = passport.photos.all()
        # print('xxxxxxxxxxx',images)
    if request.method == "POST":
        form = PassportForm(request.POST,request.FILES, instance=passport)
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
                })

        else:

            return render(request, 'passport/passport_form.html', {
                                    'form': form,'photoform':photoform})

    else:
        form = PassportForm(instance=passport)
        photoform = PhotoFormSet()
        # print('form   :  ',form)
    return render(request, 'passport/passport_form.html', {
        'form': form,'photoform':photoform,
        'passport': passport,'images':images
    })

@login_required
@ require_POST
def remove_passport(request, pk):
    passport = get_object_or_404(Passport, pk=pk)
    passport.soft_delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "passportListChanged": None,
                "showMessage": f"{passport} deleted."
            })
        })

@login_required
def remove_photo(request, id,pk):
    passport = get_object_or_404(Passport, id=id)
    if passport:
        images = passport.photos.all()
        photo = get_object_or_404(Photo, pk=pk)
        photo.delete()
        return render(request, 'passport/photoGallery.html', {
        'images':images
    })


