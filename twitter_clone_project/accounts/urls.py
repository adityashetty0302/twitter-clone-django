from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name="accounts/login.html"),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('all/', views.AllUsers.as_view(), name='all'),
    path('ajax/change-follow-status', views.change_follow_status, name='change_follow_status'),
    path('ajax/check-follow-status', views.check_follow_status, name='check_follow_status'),
]
