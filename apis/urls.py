
from .views import RegisterView
from .views import LoginView
from django.urls import path, include

urlpatterns = [
   #  path('users/',UserView.as_view()),
   #  path('users/<int:id>/', UserDetailView.as_view()),
	 
   #  path('users/generics/',UserGenericView.as_view()),
   #  path('users/generics/<int:id>/',UserGenericView.as_view()),

	#  path('auth/login/',LoginView.as_view()),
	#  path('auth/logout/',LogoutView.as_view()),
	 
	 # Modified Users
	 path('register/',RegisterView.as_view()),
	 path('login/',LoginView.as_view())
]
