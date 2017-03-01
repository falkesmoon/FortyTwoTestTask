from django.db import models


class Bio(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    jabber = models.CharField(max_length=30, blank=True, null=True)
    skype = models.CharField(max_length=30, blank=True, null=True)
    other_contacts = models.TextField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return self.name
