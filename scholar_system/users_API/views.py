from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from scholar_system.accounts.models import MasterUser
from scholar_system.users_API.serializers import MasterUserSerializer, DetailMasterUserSerializer


# class UserListCreateView(ListCreateAPIView):
#     permission_classes = [IsAdminUser, ]
#
#     serializer_class = MasterUserSerializer
#     queryset = MasterUser.objects.all()
#     filter_backends = [OrderingFilter, SearchFilter]
#     ordering_fields = ['id', 'username', ]
#     search_fields = ['email', 'first_name', 'last_name', ]
#     name = 'USERS'
#
#
# class UserUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAdminUser, ]
#
#     serializer_class = DetailMasterUserSerializer
#     queryset = MasterUser.objects.all()
#     name = 'User details'


class UserListView(ListAPIView):
    permission_classes = [IsAdminUser, ]

    serializer_class = MasterUserSerializer
    queryset = MasterUser.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['id', 'username', ]
    search_fields = ['email', 'first_name', 'last_name', ]
    name = 'USERS'


class UserDetailDeleteView(RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser, ]

    serializer_class = DetailMasterUserSerializer
    queryset = MasterUser.objects.all()
    name = 'User details'
    description = 'Removing inactive users'
