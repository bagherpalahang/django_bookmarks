from django.urls import path
from django.contrib.auth import views
from .views import user_login

urlpatterns = [
    path('login/', user_login, name='login'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('login/', views.LogoutView.as_view(), name='login'),
]
