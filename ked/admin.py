from django.contrib import admin
from .models import  Ked ,Journal
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Ked)
class KedAdmin(ImportExportModelAdmin):
    list_display = ('id',
                'title',
                'company',
                'created_at',
                'author',)
    list_filter = ('company','author',)


@admin.register(Journal)
class JournalAdmin(ImportExportModelAdmin):
    list_display = ('id',
                'ked',
                'account_credit',
                # 'sub_account_cridt',
                'account_dept',
                # 'sub_account_dept',
                'ked_date',
                'dept',
                'credit',
                'coin',
                'memo',
                'company',
                'created_at',
                'author',)
    list_filter = ('ked','account_credit','account_dept','company','author',)