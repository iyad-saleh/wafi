from django.contrib import admin

from .models import Passport, Passenger, Photo
from import_export.admin import ImportExportModelAdmin



@admin.register(Passenger)
class PassengerAdmin(ImportExportModelAdmin):

    list_display = ( 'id',
                 'first_name',
                 'last_name',
                 'father_name',
                 'mother_name',
                 'birth_date',
                 'birth_place',
                 'national_number',
                 'nationality',
                  'gender',
                 'phone',
                 'mobile',
                 'email',

                    'author',)

@admin.register(Passport)
class PassportAdmin(ImportExportModelAdmin):

    list_display = ( 'id',
                'first_name',
                 'last_name',
                 'father_name',
                 'mother_name',
                 'birth_date',
                 'birth_place',
                 'national_number',
                 'nationality',
                  'gender',
                 'phone',
                 'mobile',
                'email',
                'passport_number',
                'issue_date',
                'issue_end',
                 'issue_place',

                )
    list_filter = (
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


@admin.register(Photo)
class PhotoAdmin(ImportExportModelAdmin):
    list_display = ( 'id',
                    'image',
                    'passport')


