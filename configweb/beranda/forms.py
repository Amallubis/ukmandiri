from django.forms import ModelForm
from beranda.models import Daftar

class FormDaftar(ModelForm):
    class Meta:
        model = Daftar
        fields = '__all__'