from django.contrib import admin
from .models import Box
from import_export.admin import ImportExportModelAdmin


@admin.register(Box)
class BoxAdmin(ImportExportModelAdmin):
    list_display = ('id',
                'account',
                'company',
                'created_at',
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