from django.forms import ModelForm 
from .models import Promosi, Banner, Pengurus, Profil


class FormPromosi(ModelForm):
    class Meta:
        model = Promosi
        fields = '__all__'
        
        labels ={
            'judul':'Judul Promosi',
            'logo':'Logo Product',
            'link':'Link Website'
        }
    
class FormBanner(ModelForm):
    class Meta:
        model = Banner
        fields = '__all__' 


class FormPengurus(ModelForm):
    class Meta:
        model = Pengurus
        fields = '__all__'

        
class FormProfil(ModelForm):
    class Meta:
        model = Profil
        fields = '__all__'
