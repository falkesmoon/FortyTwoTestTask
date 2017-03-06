# -*- coding: utf-8 -*-
from unittest import TestCase
from apps.hello.models import Bio


class BioModelTest(TestCase):
    def test_bio_model(self):
        """testing model for returning right value"""
        person = Bio(name='Andrew')
        self.assertEqual(str(person), 'Andrew')

    def test_bio_model_ukr(self):
        """testing model for returning right value in ukrainian"""
        person_name = u'Андрій'
        person = Bio(name=person_name)
        self.assertEqual(str(person), 'Андрій')

    def test_bio_model_fields(self):
        """test model that all fields are presence in model"""
        person = Bio(
            name='Nick', last_name='Cave',
            date_of_birth='1957-08-22', bio='musician',
            email='nickcave@gmail.com', jabber='nickcave@42cc.co',
            skype='nickcave', other_contacts='vk.com/nickcave')
        person.save()
        data_query = Bio.objects.get(name='Nick')
        self.assertEqual(str(data_query.name), 'Nick')
        self.assertEqual(str(data_query.last_name), 'Cave')
        self.assertEqual(str(data_query.date_of_birth), '1957-08-22')
        self.assertEqual(str(data_query.bio), 'musician')
        self.assertEqual(str(data_query.email), 'nickcave@gmail.com')
        self.assertEqual(str(data_query.jabber), 'nickcave@42cc.co')
        self.assertEqual(str(data_query.skype), 'nickcave')
        self.assertEqual(str(data_query.other_contacts), 'vk.com/nickcave')
