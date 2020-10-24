import json

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import View
from rest_framework.views import APIView

from webapp.models import Photo


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class FavoriteAddView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs['pk'])
        if request.user not in photo.favorites.all():
            photo.favorites.add(request.user)
            return HttpResponse('Работает')
        else:
            return HttpResponse(status=400)


class FavoriteRemoveView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs['pk'])
        if request.user in photo.favorites.all():
            photo.favorites.remove(request.user)
            return HttpResponse('Работает')
        else:
            return HttpResponse(status=400)


