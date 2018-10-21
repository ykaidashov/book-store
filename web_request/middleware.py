import json

from web_request.models import WebRequest


class WebRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        web_request = WebRequest(
            host=request.get_host(),
            path=request.path,
            method=request.method,
            get_data=None if not request.GET else json.dumps(request.GET),
            post_data=None if not request.POST else json.dumps(request.POST),
            uri=request.build_absolute_uri(),
        )

        web_request.save()

        response = self.get_response(request)

        return response
