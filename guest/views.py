from django.shortcuts import render, redirect
from trip.models import Location , Trip
# Create your views here.
from django.db.models import Q
from django.shortcuts import get_object_or_404
from datetime import datetime as dt



def home(request):
    return render(request, 'guest/home.html',{'navbar':"home"})



def index(request):
    locations = Location.objects.all()
    return render(request, 'guest/transport.html',{
        'locations':locations,'navbar':"transport"
    })

def searchLocation(request):
    loc= request.GET.get('fromLoc')
    # print(loc)
    if loc :

        locations = Location.objects.exclude(id=loc)
    else :
        locations = Location.objects.all()
    return render(request, 'guest/locations.html', {
        'locations':locations
    })

# cityFrom
# cityTo
# company  start_time
def searchTrip(request):
    if request.method == "POST":
        fromLoc = get_object_or_404(Location, pk=request.POST['fromLoc'])
        toLoc = get_object_or_404(Location, pk=request.POST['toLoc'])

        Date=request.POST['Date']
        PassengerCount=request.POST['PassengerCount']
        if not Date:
            trips = Trip.objects.filter(
                Q(cityFrom=fromLoc)&
                Q(cityTo=toLoc)&
                Q(start_time__gte=dt.now().date())    )
        else:
            trips = Trip.objects.filter(
                Q(cityFrom=fromLoc)&
                Q(cityTo=toLoc)   &
                Q(start_time__date=Date)    )



        return render(request,'searchTrip_list.html',{'trips':trips})




def trip(request):
    return render(request, 'guest/package.html',{'navbar':"trip"})



def flight(request):
    return render(request, 'guest/flight.html',{'navbar':"flight"})

def sea(request):
    return render(request, 'guest/sea.html',{'navbar':"sea"})

def visa(request):
    return render(request, 'guest/visa.html',{'navbar':"visa"})

def hotel(request):
    return render(request, 'guest/hotel.html',{'navbar':"hotel"})

def insurance(request):
    return render(request, 'guest/insurance.html',{'navbar':"insurance"})

def document(request):
    return render(request, 'guest/document.html',{'navbar':"document"})

def shipping(request):
    return render(request, 'guest/shipping.html',{'navbar':"shipping"})

def about(request):
    return render(request, 'guest/about.html',{'navbar':"about"})
