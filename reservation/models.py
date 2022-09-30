from django.db import models
from company.models import Company
from customer.models import Customer
from django.conf import settings
from trip.models import Trip
from coin.models import Coin
from passport.models import Passport
# Create your models here.
class Reservation(models.Model):
    REVERSATIONTYPE= (
            ('1','التأشيرات'),
            ('2','تذاكرطيران'),
            ('3','تذاكربرية'),
            ('4','تذاكربحرية'),
            ('5','شحن'),
            ('6','حجزفندقي'),
            ('7','مستندات سفر'),
            ('8','عمولات'),
            ('9','تأمين صحي'),
            ('10','رحلات'),
        )
    title     = models.CharField(max_length=255,null=True,blank=True)
    reservation_type= models.CharField(choices=REVERSATIONTYPE, max_length=3 )
    Date =  models.DateTimeField()
    PNR   = models.PositiveIntegerField( null=True,blank=True)
    trip   = models.ForeignKey(Trip, null=True,blank=True, on_delete=models.SET_NULL  )
    vendor   = models.ForeignKey(Customer, null=True,blank=True, on_delete=models.SET_NULL ,related_name='vendorCompany')
    customer  = models.ForeignKey(Customer, null=True,blank=True, on_delete=models.SET_NULL ,related_name='CustomerCompany')
    pay_price = models.PositiveIntegerField()
    pay_coin  = models.ForeignKey(Coin, null=True,blank=True, on_delete=models.SET_NULL,related_name= 'payCoin' )
    sell_price = models.PositiveIntegerField()
    sell_coin  = models.ForeignKey(Coin, null=True,blank=True, on_delete=models.SET_NULL ,related_name='sellCoin' )
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Cancelled')), default=1)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title +' '+self.reservation_type

class SubReservation(models.Model):
    passport = models.ForeignKey(Passport, null=True,blank=True, on_delete=models.SET_NULL  )
    reservation = models.ForeignKey(Reservation, null=True,blank=True, on_delete=models.SET_NULL  )
    priveat_no1 = models.TextField()
    priveat_no2 = models.TextField()
    pay_price = models.PositiveIntegerField()
    pay_coin  = models.ForeignKey(Coin, null=True,blank=True, on_delete=models.SET_NULL,related_name= 'subpayCoin' )
    sell_price = models.PositiveIntegerField()
    sell_coin  = models.ForeignKey(Coin, null=True,blank=True, on_delete=models.SET_NULL ,related_name='subsellCoin'  )
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.reservation +' '+self.passport