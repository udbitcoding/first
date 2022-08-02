from http.client import responses
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from RFD.throttling import JackRateThrottle


class StudentModelViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,JackRateThrottle]


# Create your views here.
# @api_view()
# def hello_world(request):
#     return Response({'msg':'helloworld'})


# class studentAPI(APIView):
#     def get(self,request,pk= None,format=None):
#         id=request.data.get("id")
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data)
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)

#         return Response(serializer.data)

#     def post(self,request,pk= None,format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'post request'})
#         return Response(serializer.errors)

#     def put(self,request,pk= None,format=None):
#         id=request.data.get("id")
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'put request'})
#         return Response(serializer.errors)

#     def patch(self,request,pk= None,format=None):
#         id=request.data.get("id")
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'put request'})
#         return Response(serializer.errors)
        
#     def delete(self,request,pk= None,format=None):
#         id=request.data.get("id")
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         return Response({'msg':'put request'})

"""
function base views
# @api_view(['GET','POST','PUT','DELETE'])
# def hello_world(request):
#     if request.method == "GET":
#     if request.method=="POST":       
#     if request.method == "PUT":
#     if request.method == "DELETE":
"""        
        



