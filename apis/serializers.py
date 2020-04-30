from rest_framework import serializers,exceptions
from django.contrib.auth import authenticate,login
from apis.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('__all__')

class LoginSerializer(serializers.Serializer):

    phone = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type':'password'}
    )    

    def validate(self,data):

        phone = data.get('phone')
        password = data.get('password')
        

        if phone and password:

            if CustomUser.objects.filter(phone=phone).exists():

                user = authenticate(request=self.context.get('request'), phone=phone, password=password)

            else:
                msg = {
                    'status':False,
                    'details':'User not found'
                }
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'status':False,
                    'details': 'Wrong Password. Try Again'
                }
                raise serializers.ValidationError(msg, code='authorization')
        
        else:
            msg={
                'status':False,
                'details':'Phone number or password not found in request'
            }
            raise serializers.ValidationError(msg, code='authorization')        
        
        data["user"] = user

        return data