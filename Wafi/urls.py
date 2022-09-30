from django.contrib import admin
from django.urls import path, include,  re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, pages



urlpatterns = [
   path('', include('guest.urls')),
   path('dashboard/', dashboard, name='dashboard'),
    path('users/', include('users.urls')),
    path('staff/', admin.site.urls),


    path('blog', include('blog.urls')),
    path('account/', include('account.urls')),
    path('companys/', include('company.urls')),
    path('expenses/', include('expense.urls')),
    path('employee/', include('employee.urls')),
    path('reservation/', include('reservation.urls')),
    path('passport/', include('passport.urls')),
    path('customer/', include('customer.urls')),
    path('trip/', include('trip.urls')),
    path('ked/', include('ked.urls')),
    path('box/', include('box.urls')),
    re_path(r'^.*\.*', pages, name='pages'),
]


# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)