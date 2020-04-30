from rest_framework import serializers,exceptions
from django.contrib.auth import authenticate,login
# from django.contrib.auth.models import User
from apis.models import User,PhoneBook

class PhoneBookSerializer(serializers.ModelSerializer):
	class Meta:
		model = PhoneBook
		fields = '__all__'
		# First Level details in this case user details
		# depth=1
		

class UserSerializer(serializers.ModelSerializer):
	# numbers = PhoneBookSerializer(many=True)
	class Meta:
		model = User
		fields = '__all__'
   


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self,data):
		username = data.get("username","")
		password = data.get("password","")
		if username and password:
			user = authenticate(username=username,password=password)
			if user:
				if user.is_active:
					data["user"] = user
				else:
					raise exceptions.ValidationError("User not active!")
			else:
				raise exceptions.ValidationError('Unable to Login!')
		else:
			raise exceptions.ValidationError('One or more field missing')
		return data
