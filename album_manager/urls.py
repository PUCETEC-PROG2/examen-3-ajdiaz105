from django.urls import path

from . import views

# Ingresar tus URLs de la app aquí

app_name='album_manager'

urlpatterns = [
    path("", views.index, name="index"),
    path("album/<int:album_id>/", views.album, name="album"),
    path("artista/<int:artista_id>/", views.artista, name="artista"), 
    path("add_album/", views.add_album, name="add_album"),
    path("add_artista/", views.add_artista, name="add_artista"),
    path("edit_album/<int:id>/", views.edit_album, name="edit_album"), 
    path("edit_artista/<int:id>/", views.edit_artista, name="edit_artista"), 
    path("delete_album/<int:id>/", views.delete_album, name="delete_album"), 
    path("delete_artista/<int:id>/", views.delete_artista, name="delete_artista"),
]