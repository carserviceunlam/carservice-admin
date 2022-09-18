from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'session/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """ Logout view."""

    template_name = 'session/logged_out.html'
