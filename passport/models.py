from django.db import models
from PIL import Image
from django.conf import settings
from common.models import BaseModel, SoftDeleteModel


class Passenger(BaseModel, SoftDeleteModel):
    PASSENGER_GENDER =(('1','Male'),('2','Femal'))

    first_name         = models.CharField(max_length=300 )
    last_name          = models.CharField(max_length=300 )
    father_name        = models.CharField(max_length=300,blank=True, null=True )
    mother_name        = models.CharField(max_length=255,blank=True, null=True)
    birth_date         = models.DateField(blank=True, null=True)
    birth_place        = models.CharField(max_length=255,blank=True, null=True)
    national_number    =models.CharField(max_length=255,blank=True, null=True)
    nationality        =models.CharField(max_length=255,blank=True, null=True)
    gender             = models.CharField(choices=PASSENGER_GENDER ,max_length=15,default='Male' )
    phone              = models.CharField(max_length=50,verbose_name='Phone', blank=True, null=True)
    mobile             = models.CharField(max_length=50,verbose_name='mobile', blank=True, null=True)
    email              = models.EmailField(blank=True, null=True)
    avatar             = models.ImageField(null=False, blank=False,upload_to='Passenger/',default='default.jpg')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Passport(Passenger):
    passport_number= models.CharField(max_length=255,unique=True)
    issue_date= models.DateField()
    issue_end= models.DateField()
    issue_place = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name +' '+ self.last_name

class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    passport = models.ForeignKey( Passport, on_delete=models.SET_NULL, null=True, blank=True, related_name='photos')
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.passport.first_name+' '+ self.passport.last_name