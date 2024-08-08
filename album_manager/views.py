from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render,get_object_or_404
from album_manager.forms import AlbumForm,ArtistaForm
from .models import Album,Artista

# Create your views here.

def index(request):
    ##pokemons = Pokemon.objects.all() ##Select * from pokedex_pokemon
    ##pokemons = Pokemon.objects.order_by('name')##Select * from pokedex_pokemon order by name
    albums = Album.objects.order_by('type')
    artistas = Artista.objects.order_by('name')   
    template = loader.get_template('index.html')
    context = {
        'albums': albums,
        'artistas': artistas,    
        }
    return HttpResponse(template.render({'albums': albums,'artistas':artistas,}, request))

def album(request, album_id):
    ##SELECT * FROM POKEDEX_POKEMON WHERE id=pokemon_id
    album = Album.objects.get(id=album_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album   
        }
    return HttpResponse(template.render(context, request))

def artista(request, artista_id):
    artista = Artista.objects.get(id=artista_id)
    template = loader.get_template('display_artista.html')
    context = {
        'artista': artista,    
        }
    return HttpResponse(template.render(context, request))

def add_album(request):
    if request.method=='POST':
        form = AlbumForm(request.POST, request.FILES)
        form.save()
        return redirect('album_manager:index')
    else:
        form = AlbumForm()
    return render(request, 'add_album.html',{'form': form})

def add_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistaForm()
    
    return render(request, 'add_artista.html', {'form': form})  

def edit_album(request, id):
    album = get_object_or_404(Album, pk = id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm(instance=album) 
        
    return render(request, 'add_album.html', {'form': form})  

def edit_artista(request, id):
    artista = get_object_or_404(Artista, pk = id)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistaForm(instance=artista)
    
    return render(request, 'add_artista.html', {'form': form})

def delete_album(request, id):
     album = get_object_or_404(Artista, pk = id)
     album.delete()
     return redirect('album_manager:index')
 
def delete_artista(required, id):
    artista = get_object_or_404(Artista, pk = id)
    artista.delete()
    return redirect('album_manager:index')