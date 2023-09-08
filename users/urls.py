from django.urls import path
from .views import register_view, profile_view, profile_update_view

app_name = "users"
urlpatterns = [
    path("register/", register_view, name="register"),
    path("profile/<int:id>/", profile_view, name="profile"),
    path("profile/<int:id>/update/", profile_update_view, name="profile_update"),
]
