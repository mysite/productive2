# Generated by Django 3.0.4 on 2020-03-28 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='', verbose_name='Image')),
                ('thumbnail', models.FileField(upload_to='', verbose_name='Thumbnail')),
                ('pub_date', models.DateTimeField(verbose_name='Published Date')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text', models.TextField(blank=True, verbose_name='Text')),
                ('tags', models.CharField(blank=True, max_length=200, verbose_name='Tags')),
                ('category', models.SmallIntegerField(choices=[(1, 'Landscape'), (2, 'People'), (3, 'Random'), (4, 'Wall'), (5, 'Project')], default=4, verbose_name='Category')),
                ('project', models.CharField(blank=True, max_length=200, verbose_name='Project')),
                ('presentation', models.CharField(blank=True, max_length=200, verbose_name='Presentation')),
            ],
        ),
    ]