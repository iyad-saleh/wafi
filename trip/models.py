from django.db import models

from company.models import Company
from bus.models import Bus
from employee.models import Employee
from django.conf import settings
from django.urls import reverse
from datetime import datetime


# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.location



class Trip(models.Model):
    title     = models.CharField(max_length=255,null=True,blank=True)
    bus       = models.ForeignKey(Bus, on_delete=models.SET_NULL , null=True,blank=True)
    driver1   = models.ForeignKey(Employee, null=True,blank=True, on_delete=models.SET_NULL,related_name='Bus_Driver'  )
    driver2   = models.ForeignKey(Employee, null=True,blank=True, on_delete=models.SET_NULL, related_name='BusDriverHelp'  )
    cityFrom  = models.ForeignKey(Location,on_delete=models.SET_NULL, null=True,blank=True, related_name='CITY_FROM')
    cityTo    =  models.ForeignKey(Location,on_delete=models.SET_NULL, null=True,blank=True, related_name='CITY_TO')
    start_time =  models.DateTimeField()
    end_time  = models.DateTimeField( null=True,blank=True)
    company   = models.ForeignKey(Company, on_delete=models.CASCADE )
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Cancelled'),('3','Passed')), default=1)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # def status_available(self):
    #     if  self.start_time <= datetime.now():
    #         self.status = '3'
    #         # print("gggggggg")
    #         self.save()
    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('trip_edit', args=(self.id,))
        print(self.status)

        # self.status_available()
        if self.status == '2' :
            color = 'red'
        elif self.status == '3':
            color = 'blue'
        else :
            color ='green'
        return f'<a  style="color:{color};"  href="{url}" ><h5> {self.title}</h5>{self.start_time.strftime("%I:%M %p")} </a>'
