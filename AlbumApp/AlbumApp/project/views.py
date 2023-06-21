from django.shortcuts import render, redirect

from AlbumApp.project.forms import CreateProfileForm, CreateAlbumForm, DeleteAlbumForm
from AlbumApp.project.models import Profile, Album


# Create your views here.

def index_view(request):
    user = Profile.objects.first()
    albums = Album.objects.all()
    if request.method == "GET":
        form = CreateProfileForm()
        if not user:
            return render(request, 'home-no-profile.html', context={'form': form,})
        return render(request, 'home-with-profile.html', context={'user': user, 'albums': albums,})
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'home-no-profile.html', context={'form': form,})



def album_add_view(request):
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = { 'form': form, }
    return render(request, 'add-album.html', context=context)

def album_details_view(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'album-details.html', context={'album': album,})

def album_edit_view(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "GET":
        form = CreateAlbumForm(instance=album)
    else:
        form = CreateAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'edit-album.html', context={"form": form,})

def album_delete_view(request, pk):
    album = Album.objects.get(pk=pk)
    form = DeleteAlbumForm(instance=album)
    if request.method == 'POST':
        album.delete()
        return redirect('index')
    return render(request, 'delete-album.html', context={'form': form,})



def profile_details_view(request):
    user = Profile.objects.first()
    albums = len(Album.objects.all())
    return render(request, 'profile-details.html', context={'user': user, 'albums': albums,})

def profile_delete_view(request):
    user = Profile.objects.first()
    albums = Album.objects.all()
    if request.method == 'POST':
        user.delete()
        albums.delete()
        return redirect('index')
    return render(request, 'profile-delete.html')