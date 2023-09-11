from django.forms import ModelForm
from member.models import Member

class FormAddMember(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

