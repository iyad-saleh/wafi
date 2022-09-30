from django.db import models
from django.conf import settings
from company.models import Company



class Coin(models.Model):


    id            = models.IntegerField(primary_key=True)
    short_title  = models.CharField(max_length=100, blank=True, null=True,help_text="رمز مختصر ")
    long_title   = models.CharField(max_length=300, blank=True, null=True,help_text="الاسم كامل")
    active       = models.BooleanField(default=False,help_text="مستخدمة")#     الربح
    company     = models.ForeignKey(Company, null=True,blank=True, on_delete=models.SET_NULL )
    class Meta:
        verbose_name_plural = 'CURRENCIES'

    def __str__(self):
        return f'{self.short_title}'

def AddCurrency():
    from currencies import ISO_4217_CURRENCIES
    for item in ISO_4217_CURRENCIES:#(932, 'ZWL Zimbabwean dollar A/10')
        id = item[0]
        short_title = item[1][:3]
        long_title = item[1][4:]
        try:
            cc =Currency(id=id,short_title=short_title,long_title=long_title)
            cc.save()
        except Exception as e:
            print(item)
