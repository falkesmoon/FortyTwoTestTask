from models import Requests
from django.utils import timezone


class SaveRequestMiddleware(object):
    def process_response(self, request, response):
        if request.is_ajax():
            pass
        else:
            http_req = Requests(path=request.build_absolute_uri(),
                                req_time=timezone.now(),
                                method=request.method,
                                status=response.status_code)
            http_req.save()
        return response
