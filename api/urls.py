from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('user/register/', views.UserCreateView.as_view(), name='register'),
    path('user/login/', views.UserLoginView.as_view(), name='login'),
    path('user/update/', views.UserUpdateView.as_view(), name='update'),
    path('user/change-password/', views.UserChangePasswordView.as_view(), name='change-password'),
    path('user/password-reset/', views.UserPasswordResetView.as_view(), name='password-reset'),
    path('user/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('user/info/', views.UserInfoView.as_view(), name='info'),
]