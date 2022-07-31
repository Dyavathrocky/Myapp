from django import views
import django
from django.urls import  path, include
from django.contrib.auth import views as auth_views
from .views import user_login , dashboard , register

urlpatterns = [
    path('dashboard/', dashboard , name="dashboard"),
    path('', include("django.contrib.auth.urls")),
    path('register/', register , name='register'),
    #path('login/', user_login , name='login'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('change-password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    #path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    #path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    #path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    #path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),"""
]
