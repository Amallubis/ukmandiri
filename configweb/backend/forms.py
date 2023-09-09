from django.forms import ModelForm 
from .models import Promosi

class FormPromosi(ModelForm):
    class Meta:
        model = Promosi
        fields = '__all__'
        
        labels ={
            'judul':'Judul Promosi',
            'logo':'Logo Product',
            'link':'Link Website'
        }

