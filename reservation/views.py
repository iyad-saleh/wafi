import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Reservation , Reservation_airline
from .forms import ReservationForm ,AirlineReservationForm
from customer.models import Customer
from ked.models import Ked, Journal
from account.models import Account




# @login_required
# def reservation_index(request):
#     if request.user.is_MANAGER or request.user.is_RESERVATION:
#         company = request.user.company
#         form = ReservationForm()
#         form.fields['customer'].queryset = Customer.objects.filter(client=True).filter(company=company)
#         # form.fields['supplier'].queryset   = Customer.objects.filter(supplier=True).filter(company=company)

#         return render(request, 'reservation/index.html',{'form':form})
#     return HttpResponse(
#         status=403,
#         headers={
#             'HX-Trigger': json.dumps({

#                "reservationListChanged": None,
#             })
#         })




# def reservation_list(request):
#     company = request.user.company
#     reservations = Reservation.objects.filter(company=company)
#     return render(request, 'reservation/reservation_list.html', {
#         'reservations':reservations
#     })






# def add_reservation(request):
#     if request.method == "POST":
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reservation = form.save(commit=False)
#             reservation.author=request.user
#             reservation.company=request.user.company
#             reservation.save()
#             name = reservation.get_reservation_type_display()
#             account_res_type = Account.objects.filter(
#                                                 name =name ,
#                                                 account_type=reservation.reservation_type,
#                                                 company =request.user.company ).first()
#             if not account_res_type:
#                 account_res_type = Account.objects.create(
#                                   name =name ,
#                                   account_type=reservation.reservation_type ,
#                                   author= request.user,
#                                   company =request.user.company
#                                   )

#             title = ''
#             if form.cleaned_data['title']:
#                 title += form.cleaned_data['title']
#             if form.cleaned_data['reservation_type'] :
#                title += ' ' + str(form.cleaned_data['reservation_type'])
#             ked = Ked.objects.create(
#                                   title = title,
#                                   author= request.user,
#                                   company =request.user.company )
#             journal = Journal.objects.create(
#                                     ked = ked ,
#                                     account_credit =reservation.supplier.account ,
#                                     account_dept = account_res_type,
#                                     dept =   reservation.pay_price ,
#                                     credit = 0  ,
#                                     coin = reservation.pay_coin   ,
#                                     memo = 'pay '+name+' from '+str(reservation.supplier.account)   ,
#                                     author= request.user,
#                                     company =request.user.company
#                 )
#             journal = Journal.objects.create(
#                                     ked = ked ,
#                                     account_credit =account_res_type ,
#                                     account_dept = reservation.customer.account   ,
#                                     dept =   0 ,
#                                     credit = reservation.sell_price   ,
#                                     coin = reservation.sell_coin   ,
#                                     memo = 'sell '+name+' to '+str(reservation.customer.account)   ,
#                                     author= request.user,
#                                     company =request.user.company
#                 )
#             return HttpResponse(
#                 status=204,
#                 headers={
#                     'HX-Trigger': json.dumps({
#                         "reservationListChanged": None,
#                         "showMessage": f"{reservation.title} added."
#                     })
#                 })
#     else:
#         form = ReservationForm()
#     return render(request, 'reservation/reservation_form.html', {
#         'form': form,
#     })




# def edit_reservation(request, pk):
#     reservation = get_object_or_404(Reservation, pk=pk)
#     if request.method == "POST":
#         form = ReservationForm(request.POST, instance=reservation)
#         if form.is_valid():
#             reservation = form.save(commit=False)
#             reservation.author=request.user

#             reservation.save()
#             return HttpResponse(
#                 status=204,
#                 headers={
#                     'HX-Trigger': json.dumps({
#                         "reservationListChanged": None,
#                         "showMessage": f"{reservation.title} updated."
#                     })
#                 }
#             )
#     else:
#         form = ReservationForm(instance=reservation)
#     return render(request, 'reservation/reservation_form.html', {
#         'form': form,
#         'reservation': reservation,
#     })



# @ require_POST
# def remove_reservation(request, pk):
#     reservation = get_object_or_404(Reservation, pk=pk)
#     reservation.delete()
#     return HttpResponse(
#         status=204,
#         headers={
#             'HX-Trigger': json.dumps({
#                 "reservationListChanged": None,
#                 "showMessage": f"{reservation.title} deleted."
#             })
#         })




@login_required
def airline_index(request):
    if request.user.is_MANAGER or request.user.is_RESERVATION:
        company = request.user.company
        form = AirlineReservationForm()
        form.fields['customer'].queryset = Customer.objects.filter(client=True).filter(company=company)
        # form.fields['supplier'].queryset   = Customer.objects.filter(supplier=True).filter(company=company)

        return render(request, 'reservation/airline/index.html',{'form':form})
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "airlineListChanged": None,
            })
        })


def airline_list(request):
    company = request.user.company
    reservations = Reservation_airline.objects.filter(company=company)
    return render(request, 'reservation/airline/airline_list.html', {
        'reservations':reservations
    })


def edit_airline(request,pk):
    pass


def add_airline(request):

    pass


def remove_airline(request):

    pass

