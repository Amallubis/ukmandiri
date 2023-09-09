from import_export import resources
from beranda.models import Daftar

class DaftarResource(resources.ModelResource):
    class Meta:
        model = Daftar
        fields = ['tanggal','nama_lengkap','email','no_hp','keterangan']
