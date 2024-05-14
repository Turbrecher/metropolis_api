from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email','first_name','last_name']
        read_only_fields = ('id',)