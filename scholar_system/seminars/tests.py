from datetime import date, datetime, timedelta
from unittest import mock

from django.test import TestCase
from django.core.exceptions import ValidationError

from scholar_system.seminars.models import Seminar
from scholar_system.seminars.validators import validate_theme, validate_future_date


class ValidateThemeTest(TestCase):
    def test_theme_success(self):
        validate_theme('Testing the tests')

    def test_theme_expected_error(self):
        with self.assertRaises(ValidationError) as ve:
            validate_theme('Testing_the_tests.')
        self.assertIsNotNone(ve.exception)


class ValidateFutureDateTest(TestCase):
    @mock.patch('scholar_system.papers.utils.today')
    def test_validate_future_date_success(self, today_mock):
        today_mock.return_value = date(2022, 10, 12)
        validate_future_date(date(2022, 12, 12))

    @mock.patch('scholar_system.papers.utils.today')
    def test_validate_future_date_error(self, today_mock):
        today_mock.return_value = date(2022, 10, 12)
        with self.assertRaises(ValidationError) as ve:
            validate_future_date(date(2022, 9, 9))
        self.assertEquals(['Please enter a valid date for the seminar.'], ve.exception.messages)


class SeminarTest(TestCase):
    def setUp(self):
        self.seminar = Seminar(theme='Test test test', date = date.today(), time = datetime.now(), link='https://www.seminar-bg.eu/')
        self.seminar.save()

    def test_read_seminar(self):
        self.assertEqual(self.seminar.days_till, '0')
        self.assertEqual(self.seminar.theme, 'Test test test')

    def test_update_seminar_description(self):
        self.seminar.theme = 'Updated test test'
        self.seminar.date = date.today() + timedelta(days=2)
        self.seminar.save()
        self.assertEqual(self.seminar.theme, 'Updated test test')
        self.assertEqual(self.seminar.days_till, '2 days')
