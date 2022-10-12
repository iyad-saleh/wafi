from django.db import models

# Create your models here.

class Country(models.Model):

    name_ar             = models.CharField(max_length=100, blank=True, null=True)
    name_en             = models.CharField(max_length=300, blank=True, null=True)
    Alpha_2             = models.CharField(max_length=10, blank=True, null=True)
    Alpha_3             = models.CharField(max_length=10, blank=True, null=True)
    currency_alphabetic = models.CharField(max_length=100, blank=True, null=True)
    currency_name       = models.CharField(max_length=100, blank=True, null=True)
    Arabic_Formal       = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Countries'
    def __str__(self):
        return f'{self.name_ar} {self.name_en}'




class City(models.Model):
   # "Damascus","Damascus","33.5000","36.3000","Syria","SY","SYR","Dimashq","primary","2466000","1760685964"
    id          = models.IntegerField(primary_key=True)
    city        = models.CharField(max_length=100, blank=True, null=True,help_text="الاسم المحلي")
    city_ascii  = models.CharField(max_length=100, blank=True, null=True,help_text="الاسم بالانكليزية")
    country     = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    iso2        = models.CharField(max_length=100, blank=True, null=True)
    iso3        = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.city_ascii}'



class AirPort(models.Model):
    #OSDI,large_airport,Damascus International Airport,2020,AS,SY,SY-DI,Damascus,OSDI,DAM,,"36.51559829711914, 33.4114990234375"
    ident       =  models.CharField(max_length=10, blank=True, null=True)
    airport_type = models.CharField(max_length=100, blank=True, null=True)
    name         = models.CharField(max_length=300, blank=True, null=True)
    iso_country  = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    iso_region   = models.CharField(max_length=100, blank=True, null=True)
    municipality = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    iata_code    = models.CharField(max_length=100, blank=True, null=True,help_text="رمز الاتحاد الدولي")
    name_ar      = models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return f'{self.name}'


