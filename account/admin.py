from django.contrib import admin
from .models import Account
from import_export.admin import ImportExportModelAdmin


# @admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):
    list_display  = [f.name for f in Account._meta.fields]

    list_filter = ('is_deleted',)
    #             'accountType',
    #             # 'company',
    #             # 'author',
    #             )
    def get_queryset(self, request):
        qs = self.model._default_manager.all_with_deleted()
        ordering =self.ordering or ()
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    class Meta:
        model =Account
# admin.site.register(Account,AccountAdmin)


admin.site.register(Account, AccountAdmin)