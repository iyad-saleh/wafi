from django.db import models
from django.conf import settings
from account.models  import Account
from common.models import BaseModel, SoftDeleteModel

class Box(BaseModel, SoftDeleteModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE )
    # memo = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.account.name