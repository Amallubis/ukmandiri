from django.forms import ModelForm
from django.contrib.admin import widgets
from member.models import Member

class FormAddMember(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        
        widgets ={
            'tanggal_lahir':widgets.AdminDateWidget()
            
        }

