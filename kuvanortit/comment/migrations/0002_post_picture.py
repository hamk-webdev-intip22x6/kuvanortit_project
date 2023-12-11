# Generated by Django 4.2.7 on 2023-12-05 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_remove_picturefolder_main_folder_picture_private'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.picture'),
            preserve_default=False,
        ),
    ]
