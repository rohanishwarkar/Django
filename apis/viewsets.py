from rest_framework import viewsets
from .models import User,PhoneBook
from .serializers import UserSerializer,PhoneBookSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PhoneBookViewSet(viewsets.ModelViewSet):
	queryset = PhoneBook.objects.all()
	serializer_class = PhoneBookSerializer