from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def searchAirport(request):
    data=[]
    search_text=None
    if  request.GET.get('origin'):
        search_text = request.GET.get('origin')
    elif request.GET.get('destination'):
        search_text = request.GET.get('destination')
    airports = AirPort.objects.all().order_by('id')
    if search_text:

        airports= AirPort.objects.filter(Q(name__icontains=search_text)|Q(iata_code__icontains=search_text)).distinct()


    paginator = Paginator(airports, 10)
    page = request.GET.get('page', 1)
    try:
        airports = paginator.page(page)
    except PageNotAnInteger:
        airports = paginator.page(1)
    except EmptyPage:
        airports = paginator.page(paginator.num_pages)


    return render(request, 'international/searchAirport.html', {
        'airports':airports, 'page': page
    })
