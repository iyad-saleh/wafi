import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Company
from .forms import CompanyForm
from django.contrib.auth.decorators import user_passes_test
from users.models import MyUser
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



# @user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'index.html')

# @user_passes_test(lambda u: u.is_superuser)
def company_list(request):
    companys = Company.objects.all()
    if request.user.is_superuser:
        pass
    else:
        companys = Company.objects.filter(name= request.user.company.name)


    return render(request, 'company_list.html', {
        'companys':companys,
        # 'users' :users
    })

def add_company(request):
    if not request.user.is_MANAGER:
        return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "customerListChanged": None,
            })
        })
    if request.method == "POST":
        form = CompanyForm(request.POST,request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.author=request.user
            company.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "companyListChanged": None,
                        "showMessage": f"{company.name} added."
                    })
                })
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {
        'form': form,
    })

# @user_passes_test(lambda u: u.is_superuser)
def edit_company(request, pk):
    if not request.user.is_MANAGER:
        return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "customerListChanged": None,
            })
        })
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST,request.FILES, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.author=request.user
            company.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "companyListChanged": None,
                        "showMessage": f"{company.name} updated."
                    })
                }
            )
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company_form.html', {
        'form': form,
        'company': company,
    })

@user_passes_test(lambda u: u.is_superuser)
@ require_POST
def remove_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "companyListChanged": None,
                "showMessage": f"{company.name} deleted."
            })
        })




def user_list(request):
    users =MyUser.objects.filter(company=request.user.company)
    return render(request, 'users_company_list.html', {
        'users': users,
    })


def add_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            u = form.save(commit=False)
            u.company =  request.user.company
            u.save()
            username = form.cleaned_data.get('username')
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "userListChanged": None,
                        "showMessage": f"{username} added."
                    })
                })
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})




def edit_user(request, pk):
    user = get_object_or_404(MyUser, pk=pk)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "userListChanged": None,
                        "showMessage": f"{user.first_name} updated."
                    })
                }
            )
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user_form.html',context)


def remove_user(request, pk):
    user = get_object_or_404(MyUser, pk=pk)
    user.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "usersListChanged": None,
                "showMessage": f"{user.username} deleted."
            })
        })






