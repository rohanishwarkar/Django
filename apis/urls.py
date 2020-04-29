# from .views import CreateUserView
from django.urls import path, include

urlpatterns = [
    path('api/', CreateUserView.as_view()),
]