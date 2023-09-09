from django.db import models

# Create your models here.
class Daftar(models.Model):
    nama_lengkap    = models.CharField(max_length=200)
    email           = models.EmailField()
    no_hp           = models.CharField(max_length=12)
    keterangan      = models.TextField()
    upload_ktp      = models.ImageField(upload_to='upload/')
    tanggal         = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama_lengkap