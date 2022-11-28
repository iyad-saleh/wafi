from django.db import models
from PIL import Image
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel, SoftDeleteModel
from international.models import AirPort

class AirLine(BaseModel, SoftDeleteModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(default='default.jpg', upload_to='AirLine', blank=True, null=True)
    def __str__(self):
         return self.name
    def save(self, *args, **kwargs):
        super(AirLine, self).save(*args, **kwargs)

        img = Image.open(self.logo.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.logo.path)


class Flight(BaseModel, SoftDeleteModel):
    airline = models.ForeignKey(AirLine, on_delete=models.CASCADE)
    flightNo = models.CharField(max_length=255)
    def __str__(self):
         return self.flightNo


# class Airport(BaseModel, SoftDeleteModel):
#     name = models.CharField(max_length=255)
#     loc  = models.CharField(max_length=255, blank=True, null=True)
#     code = models.CharField(max_length=255, blank=True, null=True)
#     def __str__(self):
#          return self.name

    # flightList(BaseModel, SoftDeleteModel):


class FlightSchedule(BaseModel, SoftDeleteModel):
    flight            = models.ForeignKey(Flight, on_delete=models.CASCADE ,related_name='flight' )
    origin        = models.ForeignKey(AirPort, on_delete=models.CASCADE ,related_name='origin')
    destination   = models.ForeignKey(AirPort, on_delete=models.CASCADE ,related_name='destination')
    departueDate      = models.DateField( blank=True,null=True ,help_text="تاريخ المغادرة " )
    departueTime      = models.TimeField( blank=True,null=True ,help_text="تاريخ المغادرة " )
    arrivalDate       = models.DateField( blank=True,null=True ,help_text="تاريخ المغادرة " )
    arrivalTime       = models.TimeField( blank=True,null=True ,help_text="تاريخ المغادرة " )
    duration          = models.CharField(max_length=200, blank=True, null=True)
    remarks           = models.TextField(  blank=True, null=True)
    status            = models.CharField(max_length=3, choices=(  ('1','ACTIVE') ,
                                                                  ('2','SCHEDULED') ,
                                                                   ('3','DELAYED'),
                                                                   ('4','DEPARTED'), ('5','CANCELLED')))

    def __str__(self):
         return self.origin.name+'-'+ self.destination.name

class Seat(BaseModel, SoftDeleteModel): # fix for flight
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE ,related_name='flightSeat' )
    seatNo = models.PositiveSmallIntegerField( null=True,blank=True)
    seatClass = models.CharField(max_length=3, choices=(('1','Economy Class'),('2','Business Class'),('3','First Class'))  )



class FlightSeat(BaseModel, SoftDeleteModel):  # change every schedule
    seat           = models.ForeignKey(Seat, on_delete=models.CASCADE ,related_name='seat' )
    flightSchedule = models.ForeignKey(FlightSchedule, on_delete=models.CASCADE ,related_name='flightSchedule' )
    fare         = models.PositiveIntegerField()
    Status       = models.CharField(max_length=3, choices=( ('1','OPEN') , ('2','BOOKED')))

