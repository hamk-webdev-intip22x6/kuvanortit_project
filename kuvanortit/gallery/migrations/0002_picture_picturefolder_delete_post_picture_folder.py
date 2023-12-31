# Generated by Django 4.2.7 on 2023-11-29 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('tags', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='date modified')),
            ],
        ),
        migrations.CreateModel(
            name='PictureFolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='picture',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.picturefolder'),
        ),
    ]
