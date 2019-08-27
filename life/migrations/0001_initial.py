# Generated by Django 2.2.4 on 2019-08-27 07:14

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('image', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image1', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image2', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image3', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image4', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image5', pyuploadcare.dj.models.ImageField(blank=True)),
                ('contact', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=10000)),
                ('opening_days', models.CharField(default='monday to friday', max_length=50)),
                ('opening', models.IntegerField()),
                ('closing', models.IntegerField()),
                ('category', models.CharField(choices=[('Foods', 'foods'), ('Restaurants ', 'restaurants'), ('Hospitals', 'hospitals'), ('Electric Hardware', 'electric hardware'), ('Botique', 'botique'), ('Bars', 'bars'), ('Bookshop', 'bookshop'), ('Construction Material Hardware', 'construction material hardware'), ('Supermarkets', 'supermarkets')], max_length=1000)),
                ('verified', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image1', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image2', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image3', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image4', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image5', pyuploadcare.dj.models.ImageField(blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('contact', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=10000)),
                ('opening_days', models.CharField(default='monday to friday', max_length=50)),
                ('opening', models.IntegerField()),
                ('closing', models.IntegerField()),
                ('category', models.CharField(choices=[('Houses', 'houses'), ('Hostels', 'hostels'), ('Studio ', 'studio'), ('Bedsitters', 'bedsitters'), ('Flats and Apartments', 'flats and apartments'), ('Rooms', 'rooms'), ('Town Houses', 'town houses'), ('Bungalows', 'bungalows'), ('Single Rooms', 'single rooms')], max_length=1000)),
                ('verified', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('image', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image1', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image2', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image3', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image4', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image5', pyuploadcare.dj.models.ImageField(blank=True)),
                ('category', models.CharField(choices=[('Library', 'library'), ('Barber', 'barber'), ('Kibanda foods', 'kibanda foods'), ('Spa', 'spa'), ('Phone repair', 'phone repair'), ('Saloon', 'saloon'), ('Massage', 'massage'), ('Shoe repair', 'shoe repair'), ('Water point', 'water point')], max_length=1000)),
                ('price', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=10000)),
                ('contact', models.IntegerField(null=True)),
                ('opening_days', models.CharField(default='monday to friday', max_length=50)),
                ('opening', models.IntegerField()),
                ('closing', models.IntegerField()),
                ('available', models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], max_length=1000)),
                ('meeting', models.CharField(default='greenhouse', max_length=50)),
                ('verified', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(default='ads@gmail', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', pyuploadcare.dj.models.ImageField(blank=True)),
                ('bio', models.CharField(default='Hi!', max_length=30)),
                ('user', models.OneToOneField(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='life.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=10000, null=True)),
                ('bsn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='life.Business')),
                ('hsng', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='life.Housing')),
                ('svc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='life.Services')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='life.User')),
            ],
        ),
    ]
