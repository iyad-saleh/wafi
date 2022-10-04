from django.db import models
from PIL import Image
from django.conf import settings
from company.models import Company
from django.core.validators import RegexValidator
from ked.models import Journal
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from account.models  import Account
from common.models import BaseModel, SoftDeleteModel

from django.db.models.signals import pre_save
from django.dispatch import receiver



# Create your models here.
class Customer(BaseModel, SoftDeleteModel):
    account   = models.ForeignKey(Account, on_delete=models.CASCADE )
    client    = models.BooleanField(default=False)
    aircompany    = models.BooleanField(default=False)
    transportcompany    = models.BooleanField(default=False)
    seacompany    = models.BooleanField(default=False)
    visacompany    = models.BooleanField(default=False)
    backagecompany    = models.BooleanField(default=False)
    hotelcompany    = models.BooleanField(default=False)
    insurancecompany    = models.BooleanField(default=False)
    documentcompany    = models.BooleanField(default=False)
    shippingcompany    = models.BooleanField(default=False)
    logo = models.ImageField(default='default.jpg', upload_to='Customer_pics', blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    phoneNumber1 = models.CharField( max_length = 25, unique = True, blank=True, null=True)
    phoneNumber2 = models.CharField( max_length = 25, unique = True, blank=True, null=True)
    tradeRecord = models.CharField(max_length=500, blank=True, null=True)
    email       = models.EmailField( blank=True, null=True)
    webSite     =  models.URLField(max_length = 200, blank=True, null=True)
    journal     = GenericRelation(Journal)
    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = 'الشركات'


    def __str__(self):
        return self.account.name

        img = Image.open(self.logo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.logo.path)

@receiver(models.signals.pre_save, sender=Customer)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_logo = Customer.objects.get(pk=instance.pk).logo
        except Customer.DoesNotExist:
            return
        else:

            new_logo = instance.logo
            if not 'default.jpg' in   old_logo.url:
                if  old_logo.url != new_logo.url:
                    old_logo.delete(save=False)