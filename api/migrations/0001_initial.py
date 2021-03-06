# Generated by Django 3.0.6 on 2020-11-03 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('image', models.ImageField(upload_to='Category/', verbose_name='Картинка')),
                ('test', models.CharField(blank=True, max_length=150, verbose_name='На всякий случай')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(upload_to='Products/', verbose_name='Изображение')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('value', models.CharField(blank=True, max_length=50, verbose_name='Вместимость')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Описание')),
                ('test', models.CharField(blank=True, max_length=500, verbose_name='На всякий случай')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.Category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
