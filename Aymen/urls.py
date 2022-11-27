from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from users import views as user_views
from .views import dashboard, set_language_from_url
from django.views.generic import TemplateView

urlpatterns =[
    path('staff/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # path("set_language/<str:user_language>/", set_language_from_url, name="set_language_from_url"),

    path('', include('blog.urls'),name='blog'),
    path('users/', include('users.urls')),


    path('dashboard/', dashboard, name='dashboard'),
    path('airline/', include('airline.urls')),
    path('account/', include('account.urls')),
    path('companys/', include('company.urls')),
    path('expenses/', include('expense.urls')),
    path('employee/', include('employee.urls')),
    path('reservation/', include('reservation.urls'),name='reservation'),
    path('passport/', include('passport.urls')),
    path('customer/', include('customer.urls')),
    path('trip/', include('trip.urls')),
    path('ked/', include('ked.urls')),
    path('box/', include('box.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path
    path('guest/', include('guest.urls')),
   ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
