# noinspection PyUnresolvedReferences,PyPackageRequirements
from blogging.models import Post
from django.contrib.auth.models import User
from django.test import TestCase


class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = 'A good title'
        p1 = Post(title=expected, author=self.user)
        p1.save()
        actual = str(p1)
        self.assertEquals(expected, actual)
        self.assertEquals('Mr.', p1.author.first_name)
        self.assertIsNone(p1.published_at)
