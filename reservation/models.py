from django.db import models
from company.models import Company
from customer.models import Customer
from django.conf import settings
from trip.models import Trip
from coin.models import Coin
from passport.models import Passport, Passenger
from common.models import BaseModel, SoftDeleteModel




class Reservation(BaseModel, SoftDeleteModel):


    title      = models.CharField(max_length=255,null=True,blank=True)
    Date       = models.DateTimeField()
    supplier   = models.ForeignKey(Customer, null=True,blank=True, on_delete=models.SET_NULL ,related_name='suppliersCompany')
    customer   = models.ForeignKey(Customer, null=True,blank=True, on_delete=models.SET_NULL ,related_name='CustomerCompany')
    pay_price  = models.PositiveIntegerField()
    pay_coin   = models.ForeignKey(Coin, on_delete=models.CASCADE,related_name= 'payCoin' )
    sell_price = models.PositiveIntegerField()
    sell_coin  = models.ForeignKey(Coin, on_delete=models.CASCADE ,related_name='sellCoin' )
    status     = models.CharField(max_length=2, choices=(('1','Active'),('2','Cancelled'),('3','pending'),), default=1)
    def __str__(self):
        return f'{self.title}'



class Reservation_pack(Reservation):#tourist program
    pass



class Reservation_airline(Reservation):
    passenger_num    = models.PositiveSmallIntegerField( null=True,blank=True)
    PNR   = models.CharField(max_length=255, blank=True,null=True   )
    departure_date  = models.DateTimeField( blank=True,null=True ,help_text="تاريخ المغادرة " )
    airline_company   = models.CharField(max_length=255, blank=True,null=True   )
    flight_no        = models.CharField(max_length=300,blank=True,null=True)
    departure= models.CharField(max_length=255, blank=True,null=True   )
    arrival= models.CharField(max_length=255, blank=True,null=True   )
    roundtrip       = models.BooleanField(default=False,help_text="ذهاب وعودة ")
    passport       = models.ManyToManyField(Passport)
    flight_type= models.CharField(max_length=3, choices=(('1','Economy Class'),('2','Business Class'),('3','First Class'))  )
    return_date     = models.DateTimeField(  blank=True,null=True, help_text="تاريخ العودة ")

    def __str__(self):
        return f'{self.title}'



class Reservation_transport(Reservation):
    seat_number     = models.PositiveSmallIntegerField( null=True,blank=True)
    departure_date  = models.DateTimeField( blank=True,null=True ,help_text="تاريخ المغادرة " )
    transport_company   = models.CharField(max_length=255, blank=True,null=True   )
    departure    = models.CharField(max_length=255, blank=True,null=True   )
    arrival      = models.CharField(max_length=255, blank=True,null=True   )
    roundtrip       = models.BooleanField(default=False,help_text="ذهاب وعودة ")
    return_date   = models.DateTimeField(blank=True,null=True)
    passenger       = models.ManyToManyField(Passenger)



class Reservation_sea(Reservation):
    departure_date  = models.DateTimeField( blank=True,null=True ,help_text="تاريخ المغادرة " )
    sea_company   = models.CharField(max_length=255, blank=True,null=True   )
    departure= models.CharField(max_length=255, blank=True,null=True   )
    arrival= models.CharField(max_length=255, blank=True,null=True   )
    roundtrip       = models.BooleanField(default=False,help_text="ذهاب وعودة ")
    Return_date= models.DateTimeField(blank=True,null=True)
    passenger       = models.ManyToManyField(Passenger)





class Reservation_visa(Reservation):
    visa_num = models.CharField(max_length=255,blank=True,null=True)
    visa_num = models.CharField(max_length=255,blank=True,null=True)
    send_date= models.DateTimeField(blank=True,null=True)
    visa_Type =models.CharField(max_length=3, choices=(
                                            ('1','سیاحة'),
                                            ('2','عمل'),
                                            ('3','ترانزیت'),
                                            ('4','زیارة'),
                                            ('5','عائلیة'),
                                            ('6','اقامة'),

                                            )  )
    country = models.CharField(max_length=50,blank=True,null=True)
    empassy_city = models.CharField(max_length=50,blank=True,null=True)
    visa_status = models.CharField(max_length=3, choices=(
                                            ('1','Done'),
                                            ('2','pending'),
                                            ('3','Cancelled')))
    passenger       = models.ManyToManyField(Passenger)
    validUntil= models.DateField(blank=True,null=True)
    placeOfIssue=models.CharField(max_length=255,blank=True,null=True)
    dateOfIssue= models.DateField(blank=True,null=True)
    maxStay= models.PositiveSmallIntegerField( null=True,blank=True)



class Reservation_hotel(Reservation):
    pass




class Reservation_insurance(Reservation):
    pass




class Reservation_document(Reservation):
    pass




class Reservation_ship(Reservation):
    pass




class Reservation_commission(Reservation):
    pass







# class SubReservation(models.Model):
#     passport = models.ForeignKey(Passport, null=True,blank=True, on_delete=models.SET_NULL  )
#     reservation = models.ForeignKey(Reservation, null=True,blank=True, on_delete=models.SET_NULL  )
#     private_no1 = models.TextField()
#     private_no2 = models.TextField()
#     pay_price = models.PositiveIntegerField()
#     pay_coin  = models.ForeignKey(Coin, null=True,blank=True, on_delete=models.SET_NULL,related_name= 'subpayCoin' )
#     sell_price = models.PositiveIntegerField()
#     sell_coin  = models.ForeignKey(Coin, null=True,blank=True, on_delete=models.SET_NULL ,related_name='subsellCoin'  )
#     company = models.ForeignKey(Company,on_delete=models.CASCADE)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#     author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.reservation +' '+self.passport