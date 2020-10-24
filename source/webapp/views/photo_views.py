from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from webapp.models import Photo
from webapp.forms import PhotoForm


class PhotoIndexView(ListView):
    template_name = 'photo/index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ['-date']


