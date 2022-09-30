from django.contrib import admin

from .models import Passport
from import_export.admin import ImportExportModelAdmin



@admin.register(Passport)
class PassportAdmin(ImportExportModelAdmin):

    list_display = ( 'id',
            'first_name',
            'last_name',
            'father_name',
            'mother_name',
            'birth_date',
            'birth_place',
            'passport_number',
            'issue_date',
            'issue_end',
            'national_number',
            'photo',
            'nationality',
            'sex',
            'issue_place',
            'author',
                )
    list_filter = (
                'nationality',
                'author',
                )

    # def get_queryset(self, request):
    #     qs = self.model._default_manager.all_with_deleted()
    #     ordering =self.ordering or ()
    #     if ordering:
    #         qs = qs.order_by(*ordering)
    #     return qs


    # def get_Type(self, obj):
    #     return "\n".join([p.category for p in obj.category.all()])
    # def get_memo(self, obj):
    #     return obj.memo[:10]+'...'


