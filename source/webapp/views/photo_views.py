from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from webapp.models import Photo
from webapp.forms import PhotoForm


class PhotoIndexView(ListView):
    template_name = 'photo/index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ['-date']


class PhotoDetailView(DetailView):
    template_name = 'photo/photo_view.html'
    model = Photo
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    template_name = 'photo/photo_create.html'
    model = Photo

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        form.save_m2m()
        return redirect('webapp:photo_view', pk=photo.pk)

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView):
    template_name = 'photo/photo_delete.html'
    model = Photo
    success_url = reverse_lazy('webapp:index')


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'photo/photo_update.html'
    model = Photo
    form_class = PhotoForm
    permission_required = 'webapp.change_photo'

    def has_permission(self):
        photo = self.get_object()
        return super().has_permission() or photo.author == self.request.user

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})

