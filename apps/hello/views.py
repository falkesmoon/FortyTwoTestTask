from django.shortcuts import render
from apps.hello.models import Bio


def home(request):
    aboutme = Bio.objects.first()
    return render(request, 'main.html', {'aboutme': aboutme})
