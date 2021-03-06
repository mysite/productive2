# Generated by Django 3.0.4 on 2020-03-28 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=200, verbose_name='Projects')),
                ('description', models.CharField(max_length=600, verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='pictures',
            name='project_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.Projects'),
        ),
    ]
