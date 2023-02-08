from django.urls import path

from users.views import register,UserListAPIView

urlpatterns = [
    path("users/register/", register, name="register"),
    path('api/users/list', UserListAPIView.as_view(), name='user-list')
    
]