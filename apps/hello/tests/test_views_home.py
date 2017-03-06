# -*- coding: utf-8 -*-
from django.test import TestCase
from apps.hello.models import Bio
from django.core.urlresolvers import reverse


class TestView(TestCase):
    def setUp(self):
        """creating user"""
        Bio.objects.all().delete()
        person = Bio(
            name='Andrew', last_name='Minikh',
            date_of_birth='1998-04-10', bio='Student, junior python developer',
            email='falkesmoon@gmail.com', jabber='falkesmoon@42cc.co',
            skype='falkesmoon', other_contacts='vk.com/falkesmoon')
        person.save()
        self.url = reverse('home')

    def test_main_page(self):
        """ test view to render correct template and return code 200"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'main.html')
        self.assertEqual(response.status_code, 200)

    def test_render_page(self):
        """test view rendering correct data if db have 3 entries"""
        Bio.objects.create(name="qwerty", last_name="qwerty")
        Bio.objects.create(name="zxcv", last_name="zxcv")
        first_user = Bio.objects.first()
        response = self.client.get(self.url)
        self.assertEqual(response.context['aboutme'], first_user)
        self.assertIn('Andrew', response.content)
        self.assertIn('Minikh', response.content)
        self.assertIn('April 10, 1998', response.content)
        self.assertIn('Student, junior python developer', response.content)
        self.assertIn('falkesmoon@gmail.com', response.content)
        self.assertIn('falkesmoon@42cc.co', response.content)
        self.assertIn('falkesmoon', response.content)
        self.assertIn('vk.com/falkesmoon', response.content)

    def test_do_db_entries(self):
        """ test view to show message if no db entries exist"""
        Bio.objects.all().delete()       
        response = self.client.get(self.url)
        self.assertIn('No active user is found.', response.content)

    def test_cyrillic_db(self):
        """ test view if db have cyrillic symbols """
        Bio.objects.all().delete()
        Bio.objects.create(
            name='Андрій', last_name='Мініх',
            bio='Студент, розробник')
        first_user = Bio.objects.first()
        response = self.client.get(self.url)
        self.assertEqual(response.context['aboutme'], first_user)
        self.assertIn('Андрій', response.content)
        self.assertIn('Мініх', response.content)
        self.assertIn('Студент, розробник', response.content)
