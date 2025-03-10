from django.urls import path
from .views import register_user, login_user, owner_dashboard, customer_dashboard, home, profile, logout_view

urlpatterns = [
    path("", home, name="home"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("owner_dashboard/", owner_dashboard, name="owner_dashboard"),
    path("customer_dashboard/", customer_dashboard, name="customer_dashboard"),
    path("profile/", profile, name="profile"),
    path("logout/", logout_view, name="logout_view"),
]
