from django.db import models
from django.conf import settings
from company.models import Company
from customer.models import Customer
from coin.models import Coin
from django.core.validators import RegexValidator
from django.contrib.contenttypes.fields import GenericRelation



class package(models.Model):
    packagetype= (
        ('1', 'طيران'),
        ('2', 'بري'),
        ('3', 'بحري'),
        ('4', 'تكسي'),
        ('5', 'شحن'),
        ('6', 'فيزا'),
        ('7', 'تامين صحي'),
        ('8', 'سمة دخول'),
        ('9', 'شهادة صحية)'),
        )
    title     = models.CharField(max_length=255,null=True,blank=True)
    package_type= models.CharField(choices=packagetype, max_length=3,default=1 )
    start_date = models.DateField()
    create_at  = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class package_detail(models.Model):
        package_detail   = models.ForeignKey(package, on_delete=models.CASCADE )
        photo = models.ImageField(default='default.jpg', upload_to='passport_pics', blank=True, null=True)
        memo = models.TextField()
        create_at  = models.DateTimeField(auto_now_add=True)
        update_at  = models.DateTimeField(auto_now=True)
        author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     
        def __str__(self):
            return self.title


class package_suplaier(models.Model):
        package_detail   = models.ForeignKey(package, on_delete=models.CASCADE )
        package_COMPANY   = models.ForeignKey(Company, on_delete=models.CASCADE )
        price =models.PositiveIntegerField(default=0)
        coin =models.ForeignKey(Coin, on_delete=models.CASCADE )
        memo = models.TextField()
        create_at  = models.DateTimeField(auto_now_add=True)
        update_at  = models.DateTimeField(auto_now=True)
        author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     
        def __str__(self):
            return self.title            
