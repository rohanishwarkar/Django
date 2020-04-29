from rest_framework import serializers
from apis.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone','password')