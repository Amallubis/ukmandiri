from django.db import models

# Create your models here.

class Promosi(models.Model):
    judul = models.CharField(max_length=200)
    logo  = models.ImageField(upload_to='logo/')
    keterangan = models.TextField()
    link       = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.judul


class Banner(models.Model):
    judul       =models.CharField(max_length=200)
    ket_pendek  =models.TextField()
    keterangan  =models.TextField()
    slidshow    =models.ImageField(upload_to='slidshow/')
    def __str__(self):
        return self.judul + str(self.pk)