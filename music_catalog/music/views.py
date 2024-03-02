from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models
from django.shortcuts import render, get_object_or_404

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