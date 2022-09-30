from django.db import models
from PIL import Image
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(_('name'), max_length=500)
    logo = models.ImageField(default='default.jpg', upload_to='Company_pics', blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    # phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{7,15}$")
    phoneNumber1 = models.CharField( max_length = 25,  blank=True, null=True)
    phoneNumber2 = models.CharField( max_length = 25,  blank=True, null=True)
    phoneNumber3 = models.CharField( max_length = 25,  blank=True, null=True)
    phoneNumber4 = models.CharField( max_length = 25,  blank=True, null=True)

    tradeRecord = models.CharField(max_length=500, blank=True, null=True)
    email       = models.EmailField( blank=True, null=True)
    webSite     =  models.URLField(max_length = 200, blank=True, null=True)
    # category    = models.ManyToManyField(CompanyType,  related_name='type')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # staff  = models.ManyToManyField(settings.AUTH_USER_MODEL,  related_name='staff')
    class Meta:
        verbose_name = 'شركة '
        verbose_name_plural = 'الشركات'


    def __str__(self):
        return f'{self.name}'

        img = Image.open(self.logo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.logo.path)

