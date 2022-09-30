from django.db import models
from django.conf import settings
from company.models import Company
from customer.models import Customer
from django.core.validators import RegexValidator
from django.contrib.contenttypes.fields import GenericRelation
from account.models  import Account


class Bus(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE )
    company    = models.ForeignKey(Company, on_delete=models.CASCADE )
    customer = models.ForeignKey(Customer, null=True,blank=True, on_delete=models.SET_NULL, related_name='BusSubCustomer')
    start_date = models.DateField()
    busType    = models.CharField(max_length=255)
    busNumber  = models.CharField(max_length=255 ,unique=True)
    seats      = models.PositiveSmallIntegerField(default=0)
    memo       = models.TextField()
    create_at  = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.name

# class Driver(models.Model):
#     name    = models.CharField(max_length=250)
#     status = models.CharField(max_length=2, choices=(('1','سائق'),('2','معاون')), default=1)
#     company    = models.ForeignKey(Company, on_delete=models.CASCADE )
#     phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{7,15}$")
#     phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, blank=True, null=True)
#     start_date = models.DateField()
#     create_at  = models.DateTimeField(auto_now_add=True)
#     update_at  = models.DateTimeField(auto_now=True)
#     author     = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name +' '+ self.company.name

