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

        
class Pengurus(models.Model):
    nama = models.CharField(max_length=200)
    jabatan = models.CharField(max_length=200)
    foto    = models.ImageField(upload_to='pengurus/')
    fb      = models.CharField(max_length=300)
    ig      = models.CharField(max_length=300)
    tw      = models.CharField(max_length=300)
    def __str__(self):
        return self.nama


class Profil(models.Model):
    visi = models.TextField()
    misi = models.TextField()
    badanhukum = models.CharField(max_length=200)
    perizinan  = models.CharField(max_length=200)
    kemenhumham = models.CharField(max_length=200)
    nokementrian = models.CharField(max_length=200)
    noindukkoperasi = models.CharField(max_length=200)
    berdiri = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.berdiri + "|" +str(self.pk)

    
    