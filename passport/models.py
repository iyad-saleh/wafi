from django.db import models
from PIL import Image
from django.conf import settings


class Passport(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    birth_date= models.DateField()
    birth_place = models.CharField(max_length=255)
    passport_number= models.CharField(max_length=255,unique=True)
    issue_date= models.DateField()
    issue_end= models.DateField()
    national_number=models.CharField(max_length=255,unique=True)
    photo = models.ImageField(default='default.jpg', upload_to='passport_pics', blank=True, null=True)
    nationality =models.CharField(max_length=255)
    sex = models.CharField(max_length=2, choices=(('1','Male'),('2','Female')))
    issue_place = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name +' '+ self.last_name

