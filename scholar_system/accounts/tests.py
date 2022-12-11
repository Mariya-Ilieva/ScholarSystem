from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.test import TestCase
from scholar_system.accounts.validators import validate_username, validate_name


class SigninTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@test.com',
                                                         age=22, first_name='Test', last_name='Testme')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class ValidateUsernameTest(TestCase):
    def test_username_success(self):
        validate_username('Test_me')

    def test_username_expected_error(self):
        with self.assertRaises(ValidationError) as ve:
            validate_username('Test me')
        self.assertIsNotNone(ve.exception)
        self.assertEquals(['Please ensure this username contains only letters, numbers, and underscore.'], ve.exception.messages)


class ValidateNameTest(TestCase):
    def test_name_success(self):
        validate_name('Test')

    def test_username_expected_error(self):
        with self.assertRaises(ValidationError) as ve:
            validate_name('Test12')
        self.assertIsNotNone(ve.exception)
        self.assertEquals(['Please ensure this name contains only letters.'], ve.exception.messages)
