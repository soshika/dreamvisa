# Generated by Django 2.0.2 on 2019-01-13 16:52

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('image', models.FileField(default=None, upload_to='images/countries/', verbose_name='Image')),
                ('summary', models.CharField(default='', max_length=255, verbose_name='Summary')),
                ('description', tinymce.models.HTMLField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
    ]