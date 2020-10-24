from django.urls import path, include
from webapp.views import PhotoIndexView, PhotoDetailView, PhotoCreateView, PhotoDeleteView, PhotoUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoIndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_view'),
    path('photo/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/<int:pk>/update', PhotoUpdateView.as_view(), name='photo_update')
]


