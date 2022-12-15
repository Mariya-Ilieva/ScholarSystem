from rest_framework.serializers import ModelSerializer

from scholar_system.accounts.models import MasterUser


class MasterUserSerializer(ModelSerializer):
    class Meta:
        model = MasterUser
        fields = ['id', 'is_staff', 'username', 'email', 'first_name', 'last_name', 'age']


class DetailMasterUserSerializer(ModelSerializer):
    class Meta:
        model = MasterUser
        exclude = ['password', ]
