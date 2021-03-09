from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path('', views.SignupView.as_view(), name='signup'),
    #path('home/', views.HomeView.as_view(), name='home'),
    path('verify/', views.VerifyTokenView.as_view(), name='verify'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.Profile, name='profile'),
    path('updateprofile/', views.ProfileUpdateView, name='updateprofile'),
    path('add_info/', views.Account_info.as_view(), name='info'),
    path('add_info2/', views.Account_info2.as_view(), name='info2'),
    path('confirmlogout/', views.LogoutConfirmView, name='logoutconfirm'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
