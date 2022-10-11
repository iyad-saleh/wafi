from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from common.models import BaseModel, SoftDeleteModel


class Account(BaseModel, SoftDeleteModel):
    Accountchoise=(
        ('متاجرة', (
                    ('1','التأشيرات'),
                    ('2','تذاكرطيران'),
                    ('3','تذاكربرية'),
                    ('4','تذاكربحرية'),
                    ('5','شحن'),#Shipping
                    ('6','حجزفندقي'),#hotel reservation
                    ('7','مستندات سفر'),#travel documents
                    ('8','عمولات'),#commissions
                    ('9','تأمين صحي'),#health insurance
                    ('10','رحلات'),#backage

                    ('11','تحويل عملة'),#exchange
                    ('12','الاصول'),#رصيدمدور
                    ('13','أرباح وخسائر'),#Profit and loss
                    ('14','رصيد مدور'),#round balance
                    ('15','الاهتلاك'),#depreciation
                    ('16','مستحقات الموظفين'),#Employee entitlements
                    ('17','التأمينات الاجتماعية'),#social insurance
                    ('18','المصروفات'),#expenses
                    )),
        ('الشركات و الزبائن', (
            ('20', 'الزبائن'),
            ('21','شركات التأشيرات'),
            ('22','شركات نقل جوي'),
            ('23','شركات نقل بري'),
            ('24','شركات نقل بحري'),
            ('25','فنادق'),
            ('26','شركات شحن'),
            ('27','شركات تأمين صحي'),
        )),
      ('حسابات الشركة',(
            ('30','المالكين'),#owners
            ('31','الموظفين'),#employees
            ('32','الصناديق'),#Boxes
            ('33','مصاريف يومية'),#daily expenses
            ('34','الحافلات'),#buses

      )

      )

    )


    name         = models.CharField(max_length=255 )
    account_type = models.CharField(choices=Accountchoise ,max_length=4, blank=True)

    class Meta:
        unique_together = [['name', 'company']]

    def __str__(self):

        return self.name
