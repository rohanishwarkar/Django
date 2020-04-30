# from rest_framework import serializers,exceptions
# from django.contrib.auth import authenticate,login
# # from django.contrib.auth.models import User
# # from apis.models import User,PhoneBook
# from apis.models import CustomUser

# # class UserSerializer(serializers.ModelSerializer):
# # 	class Meta:
# # 		model = User
# # 		fields = ('__all__')

# class CustomUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CustomUser
#         fields = ('__all__')


# class RegistrationSerializer(serializers.ModelSerializer):

# 	# password2 				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

# 	class Meta:
# 		model = CustomUser
# 		fields = ['phone', 'password']
# 		# extra_kwargs = {
# 		# 		'password': {'write_only': True},
# 		# }	


# 	def save(self):

# 		account = CustomUser(
# 					phone=self.validated_data['phone']
# 				)
# 		password = self.validated_data['password']
# 		# password2 = self.validated_data['password2']
# 		# if password != password2:
# 		# 	raise serializers.ValidationError({'password': 'Passwords must match.'})
# 		account.set_password(password)
# 		account.save()
# 		return account


from rest_framework import serializers

from  .models import Account


class RegistrationSerializer(serializers.ModelSerializer):

	password2 				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Account
		fields = ['email', 'username', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = Account(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.save()
		return account
