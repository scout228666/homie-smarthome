from django.urls import path
from auth.views import InviteCheckView, LoginView, RegisterView

app_name = "auth"

urlpatterns = [
    path('invite/', InviteCheckView.as_view(), name='invite_check'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]