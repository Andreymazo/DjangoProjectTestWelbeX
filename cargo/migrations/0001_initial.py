# Generated by Django 4.2.1 on 2023-05-25 10:56

import cargo.management.commands.create_number
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unik_number', models.CharField(default=cargo.management.commands.create_number.unik_number_creation, editable=False)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=7)),
                ('longtitude', models.DecimalField(decimal_places=5, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude_pick_up', models.DecimalField(decimal_places=5, max_digits=7)),
                ('longtitude_pick_up', models.DecimalField(decimal_places=5, max_digits=7)),
                ('latitude_delivery', models.DecimalField(decimal_places=5, max_digits=7)),
                ('longtitude_delivery', models.DecimalField(decimal_places=5, max_digits=7)),
                ('weigh', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)], verbose_name='Вес')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Oписание')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Место доставки')),
                ('state', models.CharField(max_length=50, verbose_name='Место доставки')),
                ('zip', models.CharField(max_length=50, verbose_name='почтовый индекс')),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=7)),
                ('longtitude', models.DecimalField(decimal_places=5, max_digits=7)),
            ],
        ),
    ]
