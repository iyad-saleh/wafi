from django.urls import path, include



urlpatterns = [
    path('', include('blog.urls')),
    path('account/', include('account.urls')),
    path('companys/', include('company.urls')),
    path('expenses/', include('expense.urls')),
    path('employee/', include('employee.urls')),
    path('reservation/', include('reservation.urls')),
    path('passport/', include('passport.urls')),
    path('trip/', include('trip.urls')),

    ]