# Generated by Django 4.2.7 on 2023-12-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_post_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test_field',
            field=models.CharField(default='testi', max_length=100),
        ),
    ]
