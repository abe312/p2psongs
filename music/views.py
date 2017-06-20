#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Album
# from django.template import loader
# Create your views here.
from django.http import Http404


# def index(request):
#     all_albums = Album.objects.all()
# #    html = u"<h1>This is the music \
# #                                app homepage</h1><br/>emoji 😋"
# #     html = ''
# #     for album in all_albums:
# #         url = '/music/' + str(album.id) + '/'
# #         html += '<a href="' + str(url) + '">' \
# #         + str(album.title) + '</a><br/>'
#     template = loader.get_template("music/index.html")
#     context = {
#         'all_albums': all_albums,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


# def detail(request, album_id):
#     return HttpResponse("<h2>Details for Album id: "+str(album_id)+"</h2>")
def detail(request, album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album\
        ': album, 'error_message': 'You did not select a valid song'})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
