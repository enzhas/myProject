import qrcode
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import CostomUser

class UserAPIView (APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            u = CostomUser.objects.all()
            return Response({'users': UserSerializer(u, many=True).data})

        try:
            instance = CostomUser.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})
        
        return Response({'user': UserSerializer(instance).data})

    
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        username_path = request.data['username']
        #password = request.data['password']

        user_new = CostomUser.objects.create(
            username = request.data['username'],
            password = request.data['password'],
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            email = request.data['email'],
            role = request.data['role'],
            user_qr = f'QR/{username_path}.jpg'
        )
        id = UserSerializer(user_new).data['id']

        url = f'feedback.kz/user/{id}'

        img = qrcode.make(url)
        img.save(f'D:\\django\\feedback\\media\\QR\\{username_path}.jpg')

        #user_new.set_password(password)

        return Response({'user': UserSerializer(user_new).data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Metod PUT is not allowed"})

        try:
            instance = CostomUser.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})
        
        serializer = UserSerializer(data=request.data, instance=instance)
        serializer.is_valid()
       
        serializer.save()
        return Response({"user":serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Metod DELETE is not allowed"})

        try:
            instance = CostomUser.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})
        
        dataa = UserSerializer(instance).data
        dataa['is_active'] = False
        print(dataa)

        serializer = UserSerializer(data=dataa, instance=instance)

        serializer.is_valid()
        serializer.validated_data["is_active"] = False
        serializer.save()
        return Response({"user":serializer.data})
