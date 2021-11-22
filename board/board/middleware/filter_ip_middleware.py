from time import sleep

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allow_ips = ["127.0.0.1"]
        ip = request.META.get("REMOTE_ADDR")
        if ip not in allow_ips:
            raise PermissionDenied

        response = self.get_response(request)

        return response


class SleepMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.num_request = 0

    def __call__(self, request):
        self.num_request += 1
        if self.num_request % 5 == 0:
            sleep(5)
            return HttpResponse("Sleep 5 sec")

        response = self.get_response(request)
        return response


class SpamMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.num_request = 0

    def __call__(self, request):
        self.num_request += 1
        allow_ips = ["127.0.0.1"]
        ip = request.META.get("REMOTE_ADDR")
        if ip not in allow_ips:
            raise PermissionDenied

        response = self.get_response(request)
        return response