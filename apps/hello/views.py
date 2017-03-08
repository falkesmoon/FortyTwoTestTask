from django.shortcuts import render
from apps.hello.models import Bio, Requests
from django.http.response import HttpResponse
import json
from django.core import serializers


def home(request):
    aboutme = Bio.objects.first()
    return render(request, 'main.html', {'aboutme': aboutme})


def request_list(request):
    req_records = Requests.objects.all().order_by('-req_time')[:10]
    if request.is_ajax():
        req_records = serializers.serialize("json", req_records)
        return HttpResponse(req_records,  content_type="application/json")
    else:
        return render(request, 'requests.html', {'req_records': req_records})


def request_list_ajax(request):
    db_count = {}
    if request.is_ajax():
        db_count = {}
        db_count['records'] = Requests.objects.count()
        data = json.dumps(db_count)
        return HttpResponse(data, content_type="application/json")
