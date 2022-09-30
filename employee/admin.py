from django.contrib import admin

from .models import Employee, EmployeeType
from import_export.admin import ImportExportModelAdmin



@admin.register(EmployeeType)
class EmployeeTypeAdmin(admin.ModelAdmin):
    list_display = (
            'category',
            'author',

                )
    list_filter = (
                'category',
                'author',

)

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):

    list_display = ( 'id',
            'account',
            'get_Type',
            'company',
            'start_date',
            'salary',
            'salary_coin',
            'phone',
            'get_memo',
            'author','is_deleted',
                )
    list_filter = (
                'company',
                'author','is_deleted',
                )

    def get_queryset(self, request):
        qs = self.model._default_manager.all_with_deleted()
        ordering =self.ordering or ()
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


    def get_Type(self, obj):
        return "\n".join([p.category for p in obj.category.all()])
    def get_memo(self, obj):
        return obj.memo[:10]+'...'


