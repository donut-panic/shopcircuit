
"""shopcircuit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from accounts.views import SignUpView, ProfileUpdateView, ProfileDetailsView, UpdatedLoginView, home

# app_name = 'accounts'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('login/', UpdatedLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='log_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='base_form.html'),
    name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset.html'),
    name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
    name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_complete'),
    path('profile/<int:pk>', ProfileDetailsView.as_view(), name='profile_view'),
    path('profile/<int:pk>/update', ProfileUpdateView.as_view(), name='update_view'),
    path('profile/home', home, name='home')

]