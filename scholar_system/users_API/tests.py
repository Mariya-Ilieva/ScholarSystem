from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from scholar_system.users_API.serializers import MasterUserSerializer, DetailMasterUserSerializer


class GetAllUsersTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(username='test', password='12Test12',
                                                              email='test@test.com', age=22, first_name='Test',
                                                              last_name='Testme')
        self.user.save()

        self.user1 = get_user_model().objects.create_user(username='test1', password='11test11', email='test1@test.com',
                                             age=21, first_name='Testa', last_name='Testme')
        self.user2 = get_user_model().objects.create_user(username='test2', password='12test12', email='test2@test.com',
                                             age=22, first_name='Testo', last_name='Testmee')
        self.user3 = get_user_model().objects.create_user(username='test3', password='13test13', email='test3@test.com',
                                             age=23, first_name='Testu', last_name='Testmeee')

    def tearDown(self):
        self.user.delete()

    def test_get_all_users(self):
        self.client.login(username='test', password='12Test12')
        response = self.client.get(reverse('users'))
        users = get_user_model().objects.all()
        serializer = MasterUserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_user(self):
        self.client.login(username='test', password='12Test12')
        response = self.client.get(
            reverse('User details', kwargs={'pk': self.user1.pk}))
        user = get_user_model().objects.get(pk=self.user1.pk)
        serializer = DetailMasterUserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_user(self):
        self.client.login(username='test', password='12Test12')
        response = self.client.get(
            reverse('User details', kwargs={'pk': 15}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_delete_user(self):
        self.client.login(username='test', password='12Test12')
        response = self.client.delete(
            reverse('User details', kwargs={'pk': self.user1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_user(self):
        self.client.login(username='test', password='12Test12')
        response = self.client.delete(
            reverse('User details', kwargs={'pk': 15}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
