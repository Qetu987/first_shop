# Generated by Django 3.0.8 on 2020-07-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(default='', upload_to='pages'),
            preserve_default=False,
        ),
    ]
