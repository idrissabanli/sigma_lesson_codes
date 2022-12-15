from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied


class BlackListIPAdressMiddleware(MiddlewareMixin):
    BLACK_LIST = [
        # '192.168.155.38',
        # '192.168.155.160'
    ]

    def process_request(self, request):
        if request.META.get('REMOTE_ADDR') in self.BLACK_LIST:
            raise PermissionDenied

    # def process_response