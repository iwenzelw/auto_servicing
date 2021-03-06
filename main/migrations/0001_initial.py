# Generated by Django 3.0.5 on 2020-04-12 06:32

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название банера')),
                ('title', models.TextField(max_length=400, verbose_name='Техст На банере')),
                ('img', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='banner/%Y/%m/%d/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Банер',
                'verbose_name_plural': 'Банеры',
            },
        ),
    ]
