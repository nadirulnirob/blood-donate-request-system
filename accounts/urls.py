from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, register_view, profile, profile_edit

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]