# Generated by Django 3.0.5 on 2020-04-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50, verbose_name='Название услуги')),
                ('heading_min', models.TextField(max_length=100, verbose_name='Минимальное описание (100 сим)')),
                ('heading_max', models.TextField(max_length=1000, verbose_name='Полное описание услуги')),
                ('img', models.ImageField(upload_to='allservices/img/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Сервис услуга',
                'verbose_name_plural': 'Все сервис услуги',
            },
        ),
    ]
