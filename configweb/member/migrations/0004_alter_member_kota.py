# Generated by Django 4.2.5 on 2023-09-27 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0003_alter_member_alamat_lengkap_alter_member_kecamatan_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="kota",
            field=models.CharField(default="", max_length=200),
        ),
    ]
