from datetime import date

from django.test import TestCase
from django.urls import reverse

from scholar_system.accounts.models import Profile
from scholar_system.papers.models import Paper, Topic


class AllPapersViewTest(TestCase):
    def setUp(self):
        self.user = Profile.objects.create(username='Test', age=22, first_name='Test', last_name='Testme', user_id=6)
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def assertCollectionEmpty(self, collection):
        return self.assertEqual(0, len(collection))

    def test_all_papers_list_empty(self):
        response = self.client.get(reverse('all papers'))
        self.assertCollectionEmpty(response.context_data['paper_list'])

    def test_all_papers_list(self):
        self.publication_date = date.today()
        self.paper = Paper(created_by=self.user, description='test description', topic_id=6)
        self.paper.save()
        self.paper1 = Paper(created_by=self.user, description='description', topic_id=8)
        self.paper1.save()
        response = self.client.get(reverse('all papers'))
        self.assertEqual(2, len(list(response.context_data['paper_list'])))
        self.assertListEqual(list(response.context_data['paper_list']), [self.paper, self.paper1])


class AllTopicsViewTest(TestCase):
    def assertCollectionEmpty(self, collection):
        return self.assertEqual(0, len(collection))

    def test_all_topics_list_empty(self):
        response = self.client.get(reverse('all topics'))
        self.assertCollectionEmpty(response.context_data['topic_list'])

    def test_all_topics_list(self):
        self.topic = Topic(title='Test6')
        self.topic.save()
        self.topic1 = Topic(title='Test12')
        self.topic1.save()
        response = self.client.get(reverse('all topics'))
        self.assertEqual(2, len(list(response.context_data['topic_list'])))
        self.assertListEqual(list(response.context_data['topic_list']), [self.topic, self.topic1])
