from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class Middle1(MiddlewareMixin):
    def process_request(self, request):
        print('m1.process_request')
        # 当你写了一个返回值之后，那么他就停留在这里，把返回值呈现给用户，就不会向下传递了
        return HttpResponse('不要再往下走了')

    def process_response(self, request, response):
        print('m1.process_response')
        # 因为中间件的传递是传递的对象，所以在返回的时候也要返回一个可以供下一个中间件接收的对象
        return response
