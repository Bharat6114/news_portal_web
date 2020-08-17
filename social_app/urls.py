from django.urls import path,include   

from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("login/", views.login, name="logins"),
    path("logout/", auth_views.LogoutView.as_view(), name="logouts"),
    path('social-auth/', include('social_django.urls', namespace="social")),
]