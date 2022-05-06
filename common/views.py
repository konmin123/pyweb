from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse


class Hello(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        say = '"""<h1>Hello, World</h1>"""'

        return HttpResponse(say)


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'common/index.html')
