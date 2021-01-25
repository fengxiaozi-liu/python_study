from django.utils.deprecation import MiddlewareMixin


class M1(MiddlewareMixin):
    def process_request(self, request):
        print('m1.process_request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print(callback, callback_args, callback_kwargs)
        print('m1.process_view')

    def process_response(self, request, response):
        print('m1.process_response')
        return response


class M2(MiddlewareMixin):
    def process_request(self, request):
        print('m2.process_request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print(callback, callback_args, callback_kwargs)
        print('m2.process_view')

    def process_response(self, request, response):
        print('m2.process_response')
        return response
