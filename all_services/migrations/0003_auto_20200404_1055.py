# Generated by Django 3.0.5 on 2020-04-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_services', '0002_auto_20200404_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allservices',
            name='heading_min',
            field=models.TextField(max_length=200, verbose_name='Минимальное описание (100 сим)'),
        ),
    ]
