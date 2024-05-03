from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    next_page = reverse_lazy("index")


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("index")
