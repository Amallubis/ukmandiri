# Generated by Django 4.2.5 on 2023-09-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Daftar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nama_lengkap", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("no_hp", models.CharField(max_length=12)),
                ("keterangan", models.TextField()),
                ("upload_ktp", models.ImageField(upload_to="upload/")),
            ],
        ),
    ]
