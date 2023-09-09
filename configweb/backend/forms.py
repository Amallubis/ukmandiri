from django.forms import ModelForm 
from .models import Promosi
from .models import Banner

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


