from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from member.models import Member




class FormAddMember(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        
        widgets ={
            'tanggal_lahir': forms.DateInput({'id':'datepicker','data-date-format':'yyyy/mm/dd'})
        }
        
        

