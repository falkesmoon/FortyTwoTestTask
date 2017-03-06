from django.shortcuts import render
from apps.hello.models import Bio


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
