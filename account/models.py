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
                    ('5','شحن'),
                    ('6','حجزفندقي'),
                    ('7','مستندات سفر'),
                    ('8','عمولات'),
                    ('9','تأمين صحي'),
                    ('10','رحلات'),

                    ('11','تحويل عملة'),
                    ('12','الاصول'),
                    ('13','أرباح وخسائر'),
                    ('14','رصيدمدور'),
                    ('15','الاهتلاك'),
                    ('16','مستحقات الموظفين'),
                    ('17','التأمينات الاجتماعية'),
                    ('18','المصروفات'),
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
            ('30','المالكين'),
            ('31','الموظفين'),
            ('32','الصناديق'),
            ('33','مصاريف يومية'),
            ('34','الحافلات'),

      )

      )

    )


    name         = models.CharField(max_length=255 )
    account_type = models.CharField(choices=Accountchoise ,max_length=4, blank=True)

    class Meta:
        unique_together = [['name', 'company']]

    def __str__(self):

        return self.name
