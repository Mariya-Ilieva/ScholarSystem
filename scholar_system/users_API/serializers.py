from rest_framework import serializers
from scholar_system.accounts.models import MasterUser


class MasterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterUser
        fields = ['id', 'is_staff', 'username', 'email', 'first_name', 'last_name', 'age']


class DetailMasterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterUser
        exclude = ['password', 'last_login', ]
