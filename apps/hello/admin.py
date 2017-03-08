from django.contrib import admin
from apps.hello.models import Bio, Requests


admin.site.register(Bio)
admin.site.register(Requests)
