# Generated by Django 3.0.6 on 2020-11-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.SmallIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.SmallIntegerField(verbose_name='Цена'),
        ),
    ]
