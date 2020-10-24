from django.urls import path, include
from webapp.views import PhotoIndexView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoIndexView.as_view(), name='index')
]


