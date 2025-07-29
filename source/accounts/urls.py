from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view
app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("register/", register_view, name="register"),
]
