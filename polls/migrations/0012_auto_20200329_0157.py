# Generated by Django 3.0.4 on 2020-03-29 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_pictures_presentation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='presentation',
            field=models.CharField(choices=[('slides', 'Slides'), ('pictures', 'Pictures'), ('projects', 'Projects'), ('album', 'Album')], default='no', max_length=10),
        ),
    ]
