from rest_framework import serializers
from .models import User

class UserPushSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email','password','mobile_number','address')
        
class UserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('uid','name', 'email','mobile_number','address','created_time','modified_time')
        
class UserDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('uid','name', 'email','password','mobile_number','address','created_time','modified_time')
        
class UserUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields=('name', 'email','password','mobile_number','address',)
        
class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields=('email','password',)