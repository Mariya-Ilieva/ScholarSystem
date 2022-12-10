from datetime import date
from django.test import TestCase
from scholar_system.accounts.models import Profile
from scholar_system.papers.models import Paper


class PaperTest(TestCase):
    def setUp(self):
        self.user = Profile.objects.create(username='test', age=22, first_name='Test', last_name='Testme', user_id=6)
        self.user.save()
        self.publication_date = date.today()
        self.paper = Paper(created_by=self.user, description='test description', topic_id=6)
        self.paper.save()

    def tearDown(self):
        self.user.delete()

    def test_read_paper(self):
        self.assertEqual(self.paper.created_by, self.user)
        self.assertEqual(self.paper.description, 'test description')

    def test_update_paper_description(self):
        self.paper.description = 'updated test description'
        self.paper.save()
        self.assertEqual(self.paper.description, 'updated test description')
