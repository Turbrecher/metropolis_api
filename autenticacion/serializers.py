from rest_framework import serializers
from django.contrib.auth.models import User
     
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email','first_name','last_name']
        read_only_fields = ('id',)
        
class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email','first_name','last_name',"is_superuser"]
        read_only_fields = ('id',)