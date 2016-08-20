from django.shortcuts import render
from django.http import Http404
from .models import Album

def index(request):
    all_album = Album.objects.all()
    return render(request, 'music/index.html', {'all_album': all_album, })

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does not exists")
    return render(request, 'music/details.html', {'album': album})