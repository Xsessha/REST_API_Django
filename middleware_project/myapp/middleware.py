import time


class RequestLogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()

        response = self.get_response(request)

        end_time = time.time()

        duration = end_time - start_time

        print(f'[{request.method}] {request.path} - {duration:.3f}s')

        response['X-App-Name'] = 'MyDjangoApp'

        return response