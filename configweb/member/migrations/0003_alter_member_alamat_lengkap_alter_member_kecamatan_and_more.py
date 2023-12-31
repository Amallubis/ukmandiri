# Generated by Django 4.2.5 on 2023-09-27 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0002_alter_member_tanggal_lahir"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="alamat_lengkap",
            field=models.CharField(blank=True, default="", max_length=400),
        ),
        migrations.AlterField(
            model_name="member",
            name="kecamatan",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="member",
            name="nama_orang_tua",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="member",
            name="no_hp_pasangan",
            field=models.CharField(default="", max_length=12),
        ),
        migrations.AlterField(
            model_name="member",
            name="no_ktp",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="member",
            name="pekerjaan",
            field=models.CharField(default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="member",
            name="provinsi",
            field=models.CharField(default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="member",
            name="upload_ktp",
            field=models.ImageField(default="", upload_to="uploadktp/"),
        ),
        migrations.AlterField(
            model_name="member",
            name="upload_pas_foto",
            field=models.ImageField(default="", upload_to="uploadpasfoto/"),
        ),
    ]
