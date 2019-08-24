# Generated by Django 2.2.4 on 2019-08-24 08:12

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0002_auto_20190823_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='image1',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='image2',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='image3',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='image4',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='image5',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='housing',
            name='image1',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='housing',
            name='image2',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='housing',
            name='image3',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='housing',
            name='image4',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='housing',
            name='image5',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='services',
            name='image1',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='services',
            name='image2',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='services',
            name='image3',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='services',
            name='image4',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='services',
            name='image5',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.CharField(choices=[('Electric Hardware', 'electric hardware'), ('Construction Material Hardware', 'construction material hardware'), ('Bookshop', 'bookshop'), ('Bars', 'bars'), ('Supermarkets', 'supermarkets'), ('Foods', 'foods'), ('Restaurants ', 'restaurants'), ('Botique', 'botique'), ('Hospitals', 'hospitals')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='housing',
            name='category',
            field=models.CharField(choices=[('Studio ', 'studio'), ('Hostels', 'hostels'), ('Bedsitters', 'bedsitters'), ('Flats and Apartments', 'flats and apartments'), ('Town Houses', 'town houses'), ('Bungalows', 'bungalows'), ('Rooms', 'rooms'), ('Houses', 'houses'), ('Single Rooms', 'single rooms')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.CharField(choices=[('Library', 'library'), ('Barber', 'barber'), ('Spa', 'spa'), ('Shoe repair', 'shoe repair'), ('Massage', 'massage'), ('Water point', 'water point'), ('Phone repair', 'phone repair'), ('Kibanda foods', 'kibanda foods'), ('Saloon', 'saloon')], max_length=1000),
        ),
    ]
