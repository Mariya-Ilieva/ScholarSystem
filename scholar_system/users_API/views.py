from rest_framework import views, response, status
from scholar_system.accounts.models import MasterUser
from scholar_system.users_API.serializers import MasterUserSerializer, DetailMasterUserSerializer


class AllUsersAPIView(views.APIView):
    def get(self, request):
        users = MasterUser.objects.all().order_by('id')
        serializer = MasterUserSerializer(users, many=True)
        return response.Response({'all_users': users.count(), 'users': serializer.data})

    def post(self, request):
        serializer = MasterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class DetailsUserAPIView(views.APIView):
    def get(self, request, id):
        user = MasterUser.objects.get(pk=id)
        serializer = DetailMasterUserSerializer(user)
        return response.Response({'user': serializer.data})

    def post(self, request, id):
        user = MasterUser.objects.get(pk=id)
        serializer = DetailMasterUserSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = MasterUser.objects.get(pk=id)
        user.delete()
        return response.Response(status.HTTP_200_OK)
