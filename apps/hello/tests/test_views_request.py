from django.test import TestCase, Client
from apps.hello.models import Requests
from django.core.urlresolvers import reverse
from django.utils import timezone
import ast


class TestViewRequests(TestCase):
    def test_view_requests(self):
        """ testing request view render correctly"""
        self.url = reverse('request_list')
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'requests.html')
        self.assertEqual(response.status_code, 200)

    def test_displaying_requests(self):
        """ test view to return correct data """
        Requests.objects.all().delete()
        Requests.objects.create(
            path='http://testserver/request_list/',
            req_time='2016-12-30 10:43:53',
            method='GET',
            status=200)
        for i in range(9):
            Requests.objects.create(
                path='/' + 'test' + str(i) + '/',
                req_time='2016-12-30 10:43:53',
                method='GET',
                status=200
            )
        response = self.client.get(reverse('request_list'))
        requests = Requests.objects.all().order_by('-id')[:10]
        for request in requests:
            self.assertIn(request.path, response.content)
            self.assertIn(request.method, response.content)
            self.assertIn(str(request.status), response.content)

    def test_displaying_more_requests(self):
        """ test view returning correct data, when requests is more than 10"""
        for i in range(20):
            Requests.objects.create(
                path='http://testserver/request_list/',
                req_time=timezone.now(),
                method='GET',
                status=200)
        response = self.client.get(reverse('request_list'))
        context = response.context['req_records']
        reqs = Requests.objects.all().order_by('-id')[:10]
        for i in range(10):
            self.assertEqual(reqs[i].path, context[i].path)
            self.assertEqual(reqs[i].method, context[i].method)
            self.assertEqual(reqs[i].status, context[i].status)

    def test_returning_object_number(self):
        """ test view returning correct number of objects"""
        Requests.objects.all().delete()
        for i in range(45):
            Requests.objects.create(
                path='/' + 'test' + str(i) + '/',
                req_time='2016-12-30 10:43:53',
                method='GET',
                status=200
            )
        response = self.client.get(
                reverse('request_list_ajax'),
                content_type='application/json',
                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response_number = ast.literal_eval(response.content)
        self.assertEqual(response_number['records'], 45)