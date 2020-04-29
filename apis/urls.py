from .views import UserView,UserDetailView
from django.urls import path, include

urlpatterns = [
    path('users/',UserView.as_view()),
    path('users/<int:id>/', UserDetailView.as_view()),
]
