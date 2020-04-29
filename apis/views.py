from django.shortcuts import render

# # Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from rest_framework.generics import (
# 	CreateAPIView
# 	)
# from .serializers import UserSerializer
# from rest_framework.response import Response
# # from django.contrib.auth.models import User

# class CreateUserView(CreateAPIView):
# 	serializer_class = UserSerializer
# 	def post(self,request):
# 		phone = request.data.get('phone',False)
# 		password = request.data.get('password',False)
# 		if phone and password:
# 			serializer = UserSerializer(data = request.data)
# 			serializer.is_valid(raise_exception=True)
# 			serializer.save(data=self.request.user)
# 			return Response({
# 	            'status':True,
# 	            'details':'Registered Successfully!'
# 	        })
# 		else:
# 			return Response({
# 	            'status':False,
# 	            'details':'Error in registration.'
# 	        })
