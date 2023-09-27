from import_export import resources
from beranda.models import Daftar
from member.models import Member

class DaftarResource(resources.ModelResource):
    class Meta:
        model = Daftar
        fields = ['tanggal','nama_lengkap','email','no_hp','keterangan']

        
class MemberResource(resources.ModelResource):
    class Meta:
        model = Member
        fields = '__all__'
