from .views import UserView,UserDetailView,UserGenericView
from django.urls import path, include

urlpatterns = [
    path('users/',UserView.as_view()),
    path('users/<int:id>/', UserDetailView.as_view()),
    path('users/generics/',UserGenericView.as_view()),
    path('users/generics/<int:id>/',UserGenericView.as_view())
]
