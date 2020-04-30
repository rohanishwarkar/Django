from rest_framework import serializers,exceptions
from django.contrib.auth import authenticate,login
from apis.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('__all__')
