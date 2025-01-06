from django.http import JsonResponse, HttpResponse
from django.views import View


class HelloView(View):
    def get(self, request):
        return JsonResponse({"message": "Hello, World!"})


class HelloRoot(View):
    def get(self, request):
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello Root</title>
        </head>
        <body>
            <h1>Hello, this is root</h1>
        </body>
        </html>
        """
        return HttpResponse(html_content, content_type="text/html")
