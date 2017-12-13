
from django.shortcuts import render, get_object_or_404
from .models import Album

def index(request):
	all_albums = Album.objects.all()
	return render(request, 'demo/index.html', {'all_albums': all_albums})

def about(request):
	return render(request, 'demo/about.html')

def contact(request):
	return render(request, 'demo/contact.html')

def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'demo/detail.html', {'album': album})