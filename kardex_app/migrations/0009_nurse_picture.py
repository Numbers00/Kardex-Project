# Generated by Django 4.1.1 on 2022-10-22 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kardex_app", "0008_kardex_date_added_alter_kardex_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="nurse",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
