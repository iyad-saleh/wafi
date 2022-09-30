from django.shortcuts import render
from .forms import KedForm
from ked.models import Ked, Journal
from account.models import Account
from django.http import HttpResponse
import json

def index(request):
    if hasattr( request.user  ,'is_MANAGER' ) :
        form = KedForm()
        return render(request, 'ked/index.html',{'form': form})
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "kedListChanged": None,
            })
        })


def ked_list(request):
    company = request.user.company
    keds = Ked.objects.filter(company=company)
    return render(request, 'ked/ked_list.html', {
        'keds':keds
    })


def add_ked(request):
    pass

def edit_ked(request):
    pass

def remove_ked(request):
    pass




def journal_index(request):
    if hasattr( request.user  ,'is_MANAGER' ) :
        return render(request, 'journal/index.html')
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "journalListChanged": None,
            })
        })

def journal_list(request):
    company = request.user.company
    journals = Journal.objects.filter(company=company).order_by('-id')
    return render(request, 'journal/journal_list.html', {
        'journals':journals
    })

