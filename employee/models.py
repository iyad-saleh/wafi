from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from company.models import Company
from coin.models import Coin
from ked.models import Journal
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from account.models  import Account
from common.models import BaseModel, SoftDeleteModel


class EmployeeType(BaseModel):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Employee(BaseModel, SoftDeleteModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE )
    start_date = models.DateField( blank=True, null=True)
    category    = models.ManyToManyField(EmployeeType,  related_name='EmployeeType')
    salary = models.IntegerField()
    salary_coin = models.ForeignKey(Coin, on_delete=models.CASCADE )
    phone = models.CharField( max_length = 25, blank=True, null=True)
    memo = models.TextField(blank=True,null=True)

    # journal     = GenericRelation(Journal)

    def __str__(self):
        return self.account.name

    def get_category(self):
        return "\n".join([p.category for p in self.category.all()])
