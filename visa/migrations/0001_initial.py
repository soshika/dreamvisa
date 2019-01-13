# Generated by Django 2.0.2 on 2019-01-13 16:59

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Image')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('summary', models.CharField(max_length=255, verbose_name='Summary')),
                ('description', tinymce.models.HTMLField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Visa',
                'verbose_name_plural': 'Visas',
            },
        ),
    ]
