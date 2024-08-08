from django.db import models

# Create your models here.
class Artista(models.Model):
    name = models.CharField(max_length=60,null=False)    
    country = models.CharField(max_length=60,null=False)
    
    def __str__(self) -> str:
        return self.name
    
class Album(models.Model):
    titulo = models.CharField(max_length=30,null=False)
    year = models.DateField()
    ALBUM_TYPES={
        ('BACHATA','BACHATA'),
       ('VALLENATO','VALLENATO'),
       ('CUMBIA','CUMBIA'),
       ('ELECTRONICA','ELECTRONICA'),
       ('ROCK','ROCK'), 
       
    }
    type = models.CharField(max_length=30,choices=ALBUM_TYPES,null=False)
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE)    
    picture= models.ImageField(upload_to='album_images')
    
    def __str__(self) -> str:
        return self.titulo
