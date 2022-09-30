from django.db import models
from django.conf import settings
from company.models import Company
from account.models  import Account
from common.models import BaseModel, SoftDeleteModel


class Expense(BaseModel, SoftDeleteModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE )

    def __str__(self):
        return self.account.name
