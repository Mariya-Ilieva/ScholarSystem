from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from scholar_system.accounts.models import MasterUser
from scholar_system.users_API.serializers import MasterUserSerializer, DetailMasterUserSerializer


# class AllUsersAPIView(views.APIView):
#     def get(self, request):
#         users = MasterUser.objects.all().order_by('id')
#         serializer = MasterUserSerializer(users, many=True)
#         return response.Response({'all_users': users.count(), 'users': serializer.data})
#
#     def post(self, request):
#         serializer = MasterUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data, status.HTTP_201_CREATED)
#         return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#
# class DetailsUserAPIView(views.APIView):
#     def get(self, request, id):
#         user = MasterUser.objects.get(pk=id)
#         serializer = DetailMasterUserSerializer(user)
#         return response.Response({'user': serializer.data})
#
#     def post(self, request, id):
#         user = MasterUser.objects.get(pk=id)
#         serializer = DetailMasterUserSerializer(user, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data, status.HTTP_201_CREATED)
#         return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         user = MasterUser.objects.get(pk=id)
#         user.delete()
#         return response.Response(status.HTTP_200_OK)


class UserListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser, ]

    serializer_class = MasterUserSerializer
    queryset = MasterUser.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['id', 'username', ]
    search_fields = ['email', 'first_name', 'last_name', ]
    name = 'All users'


class UserUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser, ]

    serializer_class = DetailMasterUserSerializer
    queryset = MasterUser.objects.all()
    name = 'User details'
