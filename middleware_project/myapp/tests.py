import io
import sys

from django.http import HttpResponse
from django.test import RequestFactory, TestCase

from myapp.middleware import RequestLogMiddleware


class RequestLogMiddlewareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = RequestLogMiddleware(get_response=self.get_response)

    def get_response(self, request):
        return HttpResponse("ok")

    def test_adds_custom_header_and_logs_request(self):
        request = self.factory.get("/test-path/")

        captured_output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            response = self.middleware(request)
        finally:
            sys.stdout = original_stdout

        self.assertEqual(response["X-App-Name"], "MyDjangoApp")
        self.assertIn("[GET] /test-path/ -", captured_output.getvalue())
