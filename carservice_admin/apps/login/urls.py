from django.urls import path
from carservice_admin.apps.login import views


urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
 ]
