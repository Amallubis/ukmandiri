# Generated by Django 4.2.5 on 2023-09-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_banner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pengurus",
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
                ("nama", models.CharField(max_length=200)),
                ("jabatan", models.CharField(max_length=200)),
                ("foto", models.ImageField(upload_to="pengurus/")),
                ("fb", models.CharField(max_length=300)),
                ("ig", models.CharField(max_length=300)),
                ("tw", models.CharField(max_length=300)),
            ],
        ),
    ]
