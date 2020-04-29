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

from .serializers import UserSerializer,LoginSerializer
from .models import User
from .helpermethods import getResponse
# from django.contrib.auth.models import User

okay200 	= status.HTTP_200_OK
err400 		= status.HTTP_400_BAD_REQUEST
servererror = status.HTTP_500_INTERNAL_SERVER_ERROR

class LoginView(APIView):
	def post(self,request):
		serializer = LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data["user"]
		django_login(request,user)
		token, created =  Token.objects.get_or_create(user=user)
		return Response({'token':token.key},status=200)



class LogoutView(APIView):
	authentication_classes = (TokenAuthentication,)
	def post(self,request):
		django_logout(request)
		return Response(status=204)


class UserGenericView(generics.ListAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	lookup_field = 'id'
	authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self,request,id=None):
		if id is not None:
			return self.retrieve(request)
		return self.list(request)

	def post(self,request):
		return self.create(request)

	def put(self,request,id=None):
		return self.update(request,id)

	def delete(self,request,id):
		return self.destroy(request,id)

class UserView(APIView):
	def get(self,request):
		users = User.objects.all()
		serializer = UserSerializer(users,many=True)
		return getResponse(True,okay200,'Sucessfully Fetched Users!',serializer.data)

	def post(self,request):
		data = request.data
		try:
			phone = data.get('phone', False)
			password = data.get('password', False)
			if phone and password:
				old = User.objects.filter(phone__iexact=phone)
				if old.exists():
					return Response({
					'status':False,
			        'code':status.HTTP_400_BAD_REQUEST,
			        'details':'User already exists!',
			        'data':None
				})
				serializer = UserSerializer(data=data)
				if serializer.is_valid():
					serializer.save()
					return Response({
						'status':True,
			            'code':status.HTTP_200_OK,
			            'details':'Sucessfully Inserted User!',
			            'data':serializer.data
					})
				else:
					return Response({
						'status':False,
			            'code':status.HTTP_400_BAD_REQUEST,
			            'details':'Invalid data',
			            'data':None
					})
			else:
				return Response({
					'status':False,
					'code':status.HTTP_400_BAD_REQUEST,
					'details':'Phone or Password is Missing!',
					'data':None
				})
		except Exception as e:
			return Response({
                'status':False,
                'code':status.HTTP_500_INTERNAL_SERVER_ERROR,
                'details':"Internal Server Error",
                'data':None
            })

class UserDetailView(APIView):
	def get_object(self,id):
		try:
			return User.objects.get(id=id)
		except Exception as e:
			return None

	def get(self,request,id=None):
		instance = self.get_object(id)
		serializer = UserSerializer(instance)
		if instance is not None:
			return Response({
				'status':True,
				'code':status.HTTP_200_OK,
				'details':'Sucessfully Fetched User!',
				'data':serializer.data
			})
		return Response({
			'status':False,
			'code':status.HTTP_400_BAD_REQUEST,
			'details':'User does not exists!',
			'data':None
		})

	def put(self,request,id=None):
		data = request.data
		instance = self.get_object(id)
		if instance is not None:
			serializer = UserSerializer(instance,data=data)
			if serializer.is_valid():
				serializer.save()
				return Response({
					'status':True,
					'code':status.HTTP_200_OK,
					'details':'Sucessfully Updated User!',
					'data':serializer.data
				})
			else:
				return Response({
					'status':False,
					'code':status.HTTP_400_BAD_REQUEST,
					'details':'Invalid data!',
					'data':None
				})
		return  Response({
			'status':False,
			'code':status.HTTP_400_BAD_REQUEST,
			'details':'User not found!',
			'data':None
		})

	def delete(self,request,id=None):
		print("Inside Me")
		instance = self.get_object(id)
		if instance is not None:
			instance.delete()
			return Response({
				'status':True,
				'code':status.HTTP_200_OK,
				'details':'Sucessfully Deleted User!',
				'data':None
			})
		return Response({
			'status':False,
			'code':status.HTTP_400_BAD_REQUEST,
			'details':'User does not exists!',
			'data':None
		})
