# Generated by Django 3.0.4 on 2020-03-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_pictures_image_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
