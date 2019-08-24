# Generated by Django 2.2.4 on 2019-08-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.CharField(choices=[('Construction Material Hardware', 'construction material hardware'), ('Foods', 'foods'), ('Supermarkets', 'supermarkets'), ('Electric Hardware', 'electric hardware'), ('Bookshop', 'bookshop'), ('Botique', 'botique'), ('Restaurants ', 'restaurants'), ('Hospitals', 'hospitals'), ('Bars', 'bars')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='housing',
            name='category',
            field=models.CharField(choices=[('Bedsitters', 'bedsitters'), ('Town Houses', 'town houses'), ('Single Rooms', 'single rooms'), ('Flats and Apartments', 'flats and apartments'), ('Rooms', 'rooms'), ('Studio ', 'studio'), ('Houses', 'houses'), ('Hostels', 'hostels'), ('Bungalows', 'bungalows')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='services',
            name='available',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.CharField(choices=[('Massage', 'massage'), ('Barber', 'barber'), ('Water point', 'water point'), ('Saloon', 'saloon'), ('Kibanda foods', 'kibanda foods'), ('Library', 'library'), ('Shoe repair', 'shoe repair'), ('Phone repair', 'phone repair'), ('Spa', 'spa')], max_length=1000),
        ),
    ]
