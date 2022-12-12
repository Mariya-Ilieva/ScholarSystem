from datetime import date
from django.test import TestCase
from scholar_system.accounts.models import Profile
from scholar_system.papers.models import Paper, Comment


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


class CommentTest(TestCase):
    def setUp(self):
        self.user = Profile.objects.create(username='test', age=22, first_name='Test', last_name='Testme', user_id=6)
        self.user.save()
        self.paper = Paper(created_by=self.user, description='test description', topic_id=6)
        self.paper.save()
        self.publication_datetime = self.publication_date = date.today()
        self.comment = Comment(text='test test', commented_by=self.user, paper=self.paper)
        self.comment.save()

    def tearDown(self):
        self.user.delete()

    def test_read_comment(self):
        self.assertEqual(self.comment.commented_by, self.user)
        self.assertEqual(self.comment.text, 'test test')

    def test_update_comment_text(self):
        self.comment.text = 'updated test text'
        self.comment.save()
        self.assertEqual(self.comment.text, 'updated test text')
