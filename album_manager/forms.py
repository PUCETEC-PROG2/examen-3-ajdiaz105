from django import forms
from .models import Album,Artista

class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields='__all__'
        widgets={
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'year':forms.DateInput(attrs={'class' : 'form-control'}),  
            'type': forms.Select(attrs={'class':'form-control'}),             
            'artista':forms.Select(attrs={'class':'form-control'}),  
            'picture':forms.ClearableFileInput(attrs={'class':'form-control'}),             
        }
class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class' : 'form-control'}),
            'country':forms.TextInput(attrs={'class' : 'form-control'}),
        }