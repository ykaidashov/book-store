from django.views.generic import ListView

from web_request.models import WebRequest


class WebRequestList(ListView):
    model = WebRequest
    template_name = 'web_request/request_list.html'

    def get_queryset(self):
        queryset = WebRequest.objects.order_by('-id')[:10]

        return queryset
