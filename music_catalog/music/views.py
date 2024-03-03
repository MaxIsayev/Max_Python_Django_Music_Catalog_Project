from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
#from . import models, forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse
from django.db.models.query import QuerySet
from typing import Any
from datetime import datetime

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'albums_count': models.Album.objects.count(),
        'tracks_count': models.Track.objects.count(),
        'users_count': models.get_user_model().objects.count(),
    }
    return render(request, 'music/index.html', context)

def track_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'music/track_list.html', {
        'track_list': models.Track.objects.all(),
    })

def track_detail(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'music/track_detail.html', {
        'track': get_object_or_404(models.Track, pk=pk)
    })

class AlbumListView(generic.ListView):
    model = models.Album
    template_name = 'music/album_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        if self.request.GET.get('owner'):
            queryset = queryset.filter(owner__username=self.request.GET.get('owner'))
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user_list'] = get_user_model().objects.all().order_by('username')
        return context

class AlbumDetailView(generic.DetailView):
    model = models.Album
    template_name = 'music/album_detail.html'

class AlbumCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Album
    template_name = 'music/album_create.html'
    fields = ('name', )

    def get_success_url(self) -> str:
        messages.success(self.request, _('album created successfully').capitalize())
        return reverse('album_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class AlbumUpdateView(
        LoginRequiredMixin, 
        UserPassesTestMixin, 
        generic.UpdateView
    ):
    model = models.Album
    template_name = 'music/album_update.html'
    fields = ('name', )

    def get_success_url(self) -> str:
        messages.success(self.request, _('album updated successfully').capitalize())
        return reverse('album_list')

    def test_func(self) -> bool | None:
        return self.get_object().owner == self.request.user
    
class AlbumDeleteView(
        LoginRequiredMixin, 
        UserPassesTestMixin, 
        generic.DeleteView
    ):
    model = models.Album
    template_name = 'music/album_delete.html'

    def get_success_url(self) -> str:
        messages.success(self.request, _('album deleted successfully').capitalize())
        return reverse('album_list')

    def test_func(self) -> bool | None:
        return self.get_object().owner == self.request.user