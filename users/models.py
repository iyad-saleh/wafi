from django.db import models
from django.conf import settings
from django.utils import timezone
from PIL import Image
# from django.core.validators import RegexValidator
from company.models import Company
from customer.models import Customer
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
# from .managers import CustomUserManager
# from django.contrib.auth.validators import UnicodeUsernameValidator

from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=250, unique=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_MANAGER= models.BooleanField(default=False)
    is_RESERVATION= models.BooleanField(default=False)
    is_ACCOUNTANT= models.BooleanField(default=False)
    is_CUSTOMER= models.BooleanField(default=False)
    objects = UserManager()
    company    = models.ForeignKey(Company, blank=True, null=True, on_delete=models.SET_NULL)
    sub_customer   = models.ForeignKey(Customer, null=True,blank=True, on_delete=models.SET_NULL, related_name='sub_customer')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):
    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL , null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{7,15}$")
    phoneNumber = models.CharField(max_length = 25, unique = True, blank= True, null= True)
    # company    = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL, related_name='company')
    # customer   = models.ForeignKey(Customer, null=True,blank=True, on_delete=models.SET_NULL, related_name='customer')
    # role       = models.CharField(max_length=10, null=True,blank=True ,choices=(
    #     ('1','MANAGER'),
    #     ('2','RESERVATION'),
    #     ('3','ACCOUNTANT'),
    #     ('4','CUSTOMER'),
    #     )
    # )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
