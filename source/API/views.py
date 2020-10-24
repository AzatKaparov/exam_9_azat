import json

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import View

from API.serializers import PhotoSerializer


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class FavoriteAddView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        slr = PhotoSerializer(data=data)
        if slr.is_valid():
            slr.favorites += data['favorites']
            slr.save()
            return JsonResponse(slr.data, safe=False)
        else:
            response = JsonResponse(slr.errors, safe=False)
            response.status_code = 400
            return response






