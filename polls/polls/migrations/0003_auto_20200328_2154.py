# Generated by Django 3.0.4 on 2020-03-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200328_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('thumbnail', models.ImageField(blank=True, max_length=500, null=True, upload_to='thumbnail')),
            ],
        ),
        migrations.RemoveField(
            model_name='pictures',
            name='project',
        ),
    ]
