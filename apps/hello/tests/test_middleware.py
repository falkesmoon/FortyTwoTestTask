from django.test import TestCase
from apps.hello.models import Requests


class TestMiddleware(TestCase):

    def test_count_entries(self):
        """ test middleware correctly saving count of objects """
        req = Requests.objects.count()
        self.assertEqual(req, 0)
        self.client.get('request_list')
        req = Requests.objects.all()
        self.assertEqual(req.count(), 1)
        self.assertEqual(req.last().path, 'http://testserver/request_list')
        self.assertEqual(req.last().method, 'GET')
