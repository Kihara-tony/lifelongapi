# Generated by Django 2.2.4 on 2019-08-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.CharField(choices=[('Restaurants ', 'restaurants'), ('Botique', 'botique'), ('Foods', 'foods'), ('Hospitals', 'hospitals'), ('Electric Hardware', 'electric hardware'), ('Bookshop', 'bookshop'), ('Construction Material Hardware', 'construction material hardware'), ('Supermarkets', 'supermarkets'), ('Bars', 'bars')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='housing',
            name='category',
            field=models.CharField(choices=[('Rooms', 'rooms'), ('Bungalows', 'bungalows'), ('Studio ', 'studio'), ('Houses', 'houses'), ('Hostels', 'hostels'), ('Town Houses', 'town houses'), ('Single Rooms', 'single rooms'), ('Flats and Apartments', 'flats and apartments'), ('Bedsitters', 'bedsitters')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='services',
            name='available',
            field=models.CharField(choices=[('NO', 'no'), ('YES', 'yes')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.CharField(choices=[('Phone repair', 'phone repair'), ('Library', 'library'), ('Barber', 'barber'), ('Spa', 'spa'), ('Massage', 'massage'), ('Shoe repair', 'shoe repair'), ('Water point', 'water point'), ('Kibanda foods', 'kibanda foods'), ('Saloon', 'saloon')], max_length=1000),
        ),
    ]