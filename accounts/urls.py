from django.urls import path
from . import views

from django.conf import settings
app_name = 'accounts'

urlpatterns = [
    path('', views.SignupView.as_view(), name='signup'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('verify/', views.VerifyTokenView.as_view(), name='verify'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
