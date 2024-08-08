from django.contrib import admin
from .models import Album,Artista

# Register your models here.
@admin.register(Album)
class Albumadmin(admin.ModelAdmin):
    pass

@admin.register(Artista)
class Artistaadmin(admin.ModelAdmin):
    pass
