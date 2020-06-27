from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserPushSerializer
from .serializers import UserListSerializer
from .serializers import UserDetailsSerializer
from .serializers import UserUpdateSerializer
from .serializers import UserLoginSerializer
from .models import User
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPushSerializer
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserPushSerializer(data=request.data)
        serializer.is_valid(raise_exception=True,)
        serializer.save()
        return Response({'status':'SUCCESS','data':serializer.data,}, status=201)
        
    def get_success_headers(self, data):
        try:
            return {'status':'SUCCESS',}
        except (TypeError, KeyError):
            return {}
    
    def destroy(self, request,pk):
        if not User.objects.filter(uid=pk).exists():
            return Response({'status':'NO CONTENT'},status=200)
        instance = User.objects.all().filter(uid=pk)
        self.perform_destroy(instance)
        return Response({'status':'SUCCESS'},status=200)
    
    def perform_destroy(self, instance):
        instance.delete()
        
    def update(self, request,pk,*args, **kwargs):
        if not User.objects.filter(uid=pk).exists():
            return Response({'status':'NO CONTENT'},status=200)
        partial = kwargs.pop('partial', False)
        instance =  User.objects.get(uid=pk)
        serializer = UserUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'status':'SUCCESS'},status=200)
    
    def perform_update(self, serializer):
        serializer.save()
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
    def retrieve(self, request,pk):
        if not User.objects.filter(uid=pk).exists():
            return Response({'status':'NO CONTENT'},status=200)
        instance = User.objects.get(uid=pk)
        serializer = self.get_serializer(instance)
        return Response({'status':'SUCCESS','data':serializer.data})
    
    def login(self, request):
        try:
            if not User.objects.filter(email=request.data["email"]).exists():
                return Response({'status':'User doesnot exist'},status=200)
        except:
            return Response({'status':'EMAIL ID IS REQUIRED TO LOGIN'},status=200)
        try:
            if not User.objects.filter(email=request.data["email"],password=request.data["password"]).exists():
                return Response({'status':'Password incorrect'},status=200)
        except:
            return Response({'status':'PASSWORD IS REQUIRED TO LOGIN'},status=200)
        return Response({'status':'SUCCESS'},status=200)