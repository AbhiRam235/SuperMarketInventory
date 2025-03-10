from django.urls import path
from .views import register_user, login_user, owner_dashboard, customer_dashboard

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
]

urlpatterns += [
    path("owner_dashboard/", owner_dashboard, name="owner_dashboard"),
    path("customer_dashboard/", customer_dashboard, name="customer_dashboard"),
]
