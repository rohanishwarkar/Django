# from django.shortcuts import render
# from django.contrib.auth import login as django_login
# from django.contrib.auth import logout as django_logout

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import authentication, permissions
# from rest_framework import generics,mixins
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication


# # from knox.views import LoginView as KnoxLoginView


# # from .serializers import UserSerializer,LoginSerializer,PhoneBookSerializer
# from .serializers import CustomUserSerializer
# # from .models import User,PhoneBook
# from .models import CustomUser
# from .helpermethods import getResponse
# # from django.contrib.auth.models import User

# okay200 	= status.HTTP_200_OK
# err400 		= status.HTTP_400_BAD_REQUEST
# servererror = status.HTTP_500_INTERNAL_SERVER_ERROR


# # class RegisterView(KnoxLoginView):
# # 	permission_classes = (permissions.AllowAny, )
# # 	def post(self, request,format=None):
# # 		try:
# # 			phone = request.data.get('phone', False)
# # 			password = request.data.get('password', False)
# # 			if phone and password:
# # 				old = User.objects.filter(phone__iexact=phone)
# # 				if not old.exists():
# # 					serializer = UserSerializer(data = request.data)
# # 					if serializer.is_valid(raise_exception=True):
# # 						user_data = serializer.data
# # 						user = User.objects.create_user(phone=user_data.get('phone'), password=user_data.get('password'), first_name=user_data.get('first_name'), last_name=user_data.get('last_name'), email=user_data.get('email'), address_house_street=user_data.get('address_house_street'), address_area=user_data.get('address_area'), city=user_data.get('city'), pincode=user_data.get('pincode'), fcm_token=user_data.get('fcm_token'))
# # 						django_login(request,user)
# # 						data = super(RegisterView,self).post(request, format=None)
# # 						return Response({
# # 							'status':True,
# # 							'code':status.HTTP_200_OK,
# # 							'details':'User Registration Successful',
# # 							'data':data.data
# # 						})
# # 					else:
# # 						return Response({
# # 							'status':False,
# # 							'code':status.HTTP_400_BAD_REQUEST,
# # 							'details':'User Registration Unsuccessful',
# # 							'data':None
# # 						})
# # 				else:
# # 					return Response({
# # 						'status':False,
# # 						'code':status.HTTP_400_BAD_REQUEST,
# # 						'details':"User Already Exists!",
# # 						'data':None
# # 					})
# # 			else:
# # 				return Response({
# # 					'status':False,
# # 					'code':status.HTTP_400_BAD_REQUEST,
# # 					'details':"One of Phone or password is missing!",
# # 					'data':None
# # 				})
# # 		except Exception as e:
# # 			print(e)
# # 			return Response({
# # 						'status':False,
# # 						'code':status.HTTP_500_INTERNAL_SERVER_ERROR,
# # 						'details':"Internal Server Error",
# # 						'data':None
# # 					})



# from django.shortcuts import render
# from django.shortcuts import get_object_or_404, redirect
# from django.db import transaction
# from django.contrib.auth.signals import user_logged_out
# # from django.db.models import Q
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework import status, permissions, generics
# from rest_framework import status
# from django.http import JsonResponse
# from django.http import Http404, HttpResponse
# from django.core import serializers
# from django.db.models import Case, Sum, Value, When, Count
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from decimal import Decimal
# from .serializers import CustomUserSerializer,RegistrationSerializer
# # from .serializers import TransactionsSerializer, TransactionItemsSerializer, LoginSerializer, UserSerializer
# # from .serializers import StoreSerializer
# # from .serializers import InvoiceSerializer
# # from .serializers import RewardSerializer
# # from .serializers import ProductSerializer
# # from .serializers import UserUpdateSerializer
# # from .serializers import ChangePasswordSerializer
# # from .serializers import StoreUpdateSerializer
# # from .serializers import CustomerSerializer
# # from .serializers import ProductUpdateSerializer
# # from .serializers import DashboardBroadcastSerializer
# # from .serializers import PaymentsSerializer
# import random
# import requests
# import uuid
# from .models import CustomUser	
# # from .models import e90Items, Transactions, TransactionItems, User, PhoneOTP
# # from .models import Store, StoreUserAccess, StoreUserAccessType, SubscriptionType
# # from .models import Invoice, Reward, Product, Customer
# # from .models import DashboardBroadcast
# # from .models import RewardValues
# # from .models import Payments
# # from .e90api.e90_live_api import e90livebarcodecheck
# # from .e90api.e90_live_api import checkInE90

# # from .payment_service import checkPaymentStatusPayTM, createPaymentPaytm

# # from knox.views import LoginView as KnoxLoginView
# # from knox.views import LogoutView as KnoxLogoutView
# # from knox.auth import TokenAuthentication
# from django.contrib.auth import login
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
# import traceback
# from datetime import datetime, timedelta, date
# import pytz
# import json
# from rest_framework.exceptions import ParseError
# import os
# from django.conf import settings
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile

# # from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
# # from azure.storage.blob import generate_blob_sas

# # from .utility import getStoreAdmins, isStoreAdmin, barcode_is_valid, barcode_is_rare, deriveRewardValue, barcode_is_not_isbn

# # from .firebase_service import sendUserCustomNotification
# # from .firebase_service import sendUsersCustomNotification

# from django.template import loader
# from django.template.loader import get_template

# import hashlib
# from hashlib import blake2b


# class RegisterView(APIView):
# 	def post(self,request):
# 		serializer = RegistrationSerializer(data=request.data)
# 		data = {}
# 		if serializer.is_valid():
# 			user = serializer.save()
# 			data['phone'] = user.phone
# 			token = Token.objects.get(user=user).key
# 			data['token'] = token
# 		else:
# 			data = serializer.errors
# 		return Response(data)
# # import firebase_admin
# # from firebase_admin import credentials
# # from . import app_strings



# # def getFirebaseAdmin():

# #     try:
# #         cred = credentials.Certificate(settings.GOOGLE_APPLICATION_CREDENTIALS_SERVER)
# #         firebase_admin.initialize_app(cred)
# #         return True

# #     except Exception as e:

# #         traceback.print_exc()

# #         return False

# # firebaseAdmin = getFirebaseAdmin()



# # Create your views here

# # class Register(KnoxLoginView):

# #     permission_classes = (permissions.AllowAny, )

# #     @transaction.atomic
# #     def post(self, request,format=None):

# #         try:
# #             phone = request.data.get('phone', False)
# #             password = request.data.get('password', False)


# #             if phone and password:
# #                 old = User.objects.filter(phone__iexact=phone)

# #                 if not old.exists():
# #                   #   old = old.first()
# #                     validated = True

# #                     if validated:
# #                         serializer = UserSerializer(data = request.data)


# #                         if serializer.is_valid(raise_exception=True):

# #                             user_data = serializer.data
# #                             user = User.objects.create_user(phone=user_data.get('phone'), password=user_data.get('password'), first_name=user_data.get('first_name'), last_name=user_data.get('last_name'), email=user_data.get('email'), address_house_street=user_data.get('address_house_street'), address_area=user_data.get('address_area'), city=user_data.get('city'), pincode=user_data.get('pincode'), fcm_token=user_data.get('fcm_token'))

# #                            #  old.delete()

# #                            #  StoreUserAccess.objects.filter(phone=phone).update(status=True)

# #                             login(request,user)


# #                             data = super().post(request, format=None)

# #                             return Response({
# #                                 'status':True,
# #                                 'code':status.HTTP_200_OK,
# #                                 'details':'User Registration Successful',
# #                                 'data':data.data
# #                             })
# #                         else:
# #                             return Response({
# #                                 'status':False,
# #                                 'code':status.HTTP_400_BAD_REQUEST,
# #                                 'details':'User Registration Unsuccessful',
# #                                 'data':None
# #                             })

# #                     else:
# #                         return Response({
# #                             'status':False,
# #                             'code': status.HTTP_400_BAD_REQUEST,
# #                             'details':'OTP not verified. Please try registering again!',
# #                             'data':None
# #                         })


# #                 else:
# #                     return Response({
# #                         'status':False,
# #                         'code':status.HTTP_400_BAD_REQUEST,
# #                         'details':"OTP Doesn't Exist",
# #                         'data':None
# #                     })

# #             else:
# #                 return Response({
# #                     'status':False,
# #                     'code':status.HTTP_400_BAD_REQUEST,
# #                     'details':"One of Phone or password is missing!",
# #                     'data':None
# #                 })
# #         except Exception as e:
# #             print(e)
# #             return Response({
# #                     'status':False,
# #                     'code':status.HTTP_500_INTERNAL_SERVER_ERROR,
# #                     'details':"Internal Server Error",
# #                     'data':None
# #                 })


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import RegistrationSerializer
from .models import Account
from rest_framework.authtoken.models import Token

# Register
# Response: https://gist.github.com/mitchtabian/c13c41fa0f51b304d7638b7bac7cb694
# Url: https://<your-domain>/api/account/register
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):

	if request.method == 'POST':
		data = {}
		# email = request.data.get('email', '0').lower()
		# if validate_email(email) != None:
		# 	data['error_message'] = 'That email is already in use.'
		# 	data['response'] = 'Error'
		# 	return Response(data)

		# username = request.data.get('username', '0')
		# if validate_username(username) != None:
		# 	data['error_message'] = 'That username is already in use.'
		# 	data['response'] = 'Error'
		# 	return Response(data)

		serializer = RegistrationSerializer(data=request.data)
		
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
			data['pk'] = account.pk
			token = Token.objects.get(user=account).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)