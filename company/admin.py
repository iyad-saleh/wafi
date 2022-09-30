from django.contrib import admin

from .models import Company#,CompanyType

# admin.site.register(Company)
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = ( 'id',
                'name',
                # 'logo',
                'get_address',
                'phoneNumber1',
                # 'phoneNumber2',
                'get_tradeRecord',
                # 'email',
                # 'get_staff',
                # 'webSite',
                # 'create_at',
                'update_at',
                # 'author',
                )
    list_filter = (
                # 'category',
                'create_at',
                'update_at',
                # 'author',
                )
    # def get_staff(self, obj):
    #     return "\n".join([p.get_full_name() for p in obj.staff.all()])
    def get_tradeRecord(self, obj):
        if obj.tradeRecord:
            return obj.tradeRecord[:10]+'...'
    def get_address(self, obj):
        if obj.address:
            return obj.address[:10]+'...'
# admin.site.register(CompanyType)
# @admin.register(CompanyType)
# class CompanyTypeAdmin(admin.ModelAdmin):
#     list_display = (
#              'category',
#             'author',
#             'create_at',
#             'update_at',
#                 )
#     list_filter = (
#                 'category',
#                 'author',
#                 'create_at',
#                 'update_at',
# )
