# Generated by Django 4.2.5 on 2023-09-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("beranda", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="daftar",
            name="tanggal",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
