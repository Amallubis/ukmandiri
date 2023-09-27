from django.db import models
# Create your models here.

class Member(models.Model):
    nama_lengkap = models.CharField(max_length=200)
    PRIA = 'L'
    PEREMPUAN = 'P'
    JENIS_KELAMIN = [
        (PRIA, 'pria'),
        (PEREMPUAN, 'Perempuan'),
    ]
    jenis_kelamin = models.CharField(max_length=20, choices=JENIS_KELAMIN, default=PRIA)

    AGAMA = [
        ('Islam','Islam'),
        ('Kristen','Kristen'),
        ('Katolik','Katolik'),
        ('Budha','Budha'),
        ('Hindu','Hindu'),
        ('Konghucu','Konghucu')
    ]
    agama = models.CharField(max_length=10, choices=AGAMA, default='Islam')
    tempat_lahir = models.CharField(max_length=300,blank=True)
    tanggal_lahir = models.DateField(help_text='Tanggal Lahir', default='1988/01/01')
    alamat_lengkap = models.CharField(max_length=400, blank=True, default='')
    kecamatan = models.CharField(max_length=200,default='')
    kota = models.CharField(max_length=200, default='')
    provinsi = models.CharField(max_length=300, default='')
    no_hp = models.CharField(max_length=12,default='+62')
    no_ktp = models.CharField(max_length=20, default='')
    pekerjaan = models.CharField(max_length=300,default='')
    KELUARGA =[
        ('Suami','Suami'),
        ('Istri','Istri'),
        ('Anak','Anak'),
        ('Menantu','Menantu'),
        ('Cucu','Cucu'),
        ('Keponakan','Keponakan'),
        ('Orang Tua','Orang Tua'),
        ('Mertua','Mertua'),
        
    ]
    status_dalam_keluarga = models.CharField(max_length=200, choices=KELUARGA, default='Suami')
    nama_orang_tua = models.CharField(max_length=200,default='')
    no_hp_pasangan = models.CharField(max_length=12, default='')
    upload_ktp      =models.ImageField(upload_to='uploadktp/', default='')
    upload_pas_foto =models.ImageField(upload_to='uploadpasfoto/', default='')


    def __str__(self):
        return self.nama_lengkap