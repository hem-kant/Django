from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'MyMusicapp/index.html',  {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("No data found custom 404 message!!!")
    return render(request, 'MyMusicapp/detail.html',{'album': album} )
