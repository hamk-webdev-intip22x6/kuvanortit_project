# Generated by Django 4.2.7 on 2023-11-30 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_picture_picturefolder_delete_post_picture_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturefolder',
            name='main_folder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.picturefolder'),
        ),
    ]
