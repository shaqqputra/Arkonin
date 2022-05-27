from django.contrib.auth import views as auth_views
from django.urls import path
from .views import UserRegisterView, UserUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('<int:pk>/edit_profile/', UserUpdateView.as_view(), name="update-profile"),
]
