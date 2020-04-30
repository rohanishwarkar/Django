from django.shortcuts import render
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


from knox.views import LoginView as KnoxLoginView
from .serializers import CustomUserSerializer
from .serializers import LoginSerializer
from .models import CustomUser
from .helpermethods import getResponse

okay200 	= status.HTTP_200_OK
err400 		= status.HTTP_400_BAD_REQUEST
servererror = status.HTTP_500_INTERNAL_SERVER_ERROR


class RegisterView(KnoxLoginView):
	permission_classes = (permissions.AllowAny, )
	def post(self, request,format=None):
		try:
			phone = request.data.get('phone', False)
			password = request.data.get('password', False)
			if phone and password:
				old = CustomUser.objects.filter(phone__iexact=phone)
				if not old.exists():
					serializer = CustomUserSerializer(data = request.data)
					if serializer.is_valid(raise_exception=True):
						user_data = serializer.data
						user = CustomUser.objects.create_user(phone=user_data.get('phone'), password=user_data.get('password'), first_name=user_data.get('first_name'), last_name=user_data.get('last_name'), email=user_data.get('email'), address_house_street=user_data.get('address_house_street'), address_area=user_data.get('address_area'), city=user_data.get('city'), pincode=user_data.get('pincode'), fcm_token=user_data.get('fcm_token'))
						django_login(request,user)
						data = super().post(request, format=None)
						return Response({
							'status':True,
							'code':status.HTTP_200_OK,
							'details':'User Registration Successful',
							'data':data.data
						})
					else:
						return Response({
							'status':False,
							'code':status.HTTP_400_BAD_REQUEST,
							'details':'User Registration Unsuccessful',
							'data':None
						})
				else:
					return Response({
						'status':False,
						'code':status.HTTP_400_BAD_REQUEST,
						'details':"User Already Exists!",
						'data':None
					})
			else:
				return Response({
					'status':False,
					'code':status.HTTP_400_BAD_REQUEST,
					'details':"One of Phone or password is missing!",
					'data':None
				})
		except Exception as e:
			print(e)
			return Response({
						'status':False,
						'code':status.HTTP_500_INTERNAL_SERVER_ERROR,
						'details':"Internal Server Error",
						'data':None
					})

class LoginView(KnoxLoginView):
		permission_classes = (permissions.AllowAny, )
		def post(self, request, format=None):
			fcm_token = request.data.get('fcm_token', False)
			serializer = LoginSerializer(data=request.data)

			if serializer.is_valid(raise_exception=False):
				user = serializer.validated_data['user']
				if fcm_token == "" or fcm_token is None:
						django_login(request,user)
				else:
						user.fcm_token = fcm_token
						user.save()
						django_login(request, user)

				django_login(request, user)
				data = super().post(request, format=None)
				if user.fcm_token == "" or user.fcm_token == None:
						return Response({
							'status':True,
							'code':status.HTTP_200_OK,
							'details':"Login Successful! Notifications Disabled",
							'data':data.data
						})
				else:
						return Response({
							'status':True,
							'code':status.HTTP_200_OK,
							'details':"Login Successful!",
							'data':data.data
						})
			else:
				if serializer.errors.get('details'):
						return Response({
							'status':False,
							'code':status.HTTP_400_BAD_REQUEST,
							'details':serializer.errors['details'][0],
							'data':None
						})

				else:
						return Response({
							'status':False,
							'code':status.HTTP_400_BAD_REQUEST,
							'details':"Unable to Login!",
							'data':None
						})

