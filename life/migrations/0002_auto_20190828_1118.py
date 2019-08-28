# Generated by Django 2.2.4 on 2019-08-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.CharField(choices=[('Electric Hardware', 'electric hardware'), ('Construction Material Hardware', 'construction material hardware'), ('Hospitals', 'hospitals'), ('Botique', 'botique'), ('Foods', 'foods'), ('Bookshop', 'bookshop'), ('Restaurants ', 'restaurants'), ('Bars', 'bars'), ('Supermarkets', 'supermarkets')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='housing',
            name='category',
            field=models.CharField(choices=[('Bedsitters', 'bedsitters'), ('Houses', 'houses'), ('Rooms', 'rooms'), ('Single Rooms', 'single rooms'), ('Flats and Apartments', 'flats and apartments'), ('Studio ', 'studio'), ('Hostels', 'hostels'), ('Town Houses', 'town houses'), ('Bungalows', 'bungalows')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='services',
            name='available',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.CharField(choices=[('Shoe repair', 'shoe repair'), ('Saloon', 'saloon'), ('Library', 'library'), ('Kibanda foods', 'kibanda foods'), ('Barber', 'barber'), ('Phone repair', 'phone repair'), ('Massage', 'massage'), ('Water point', 'water point'), ('Spa', 'spa')], max_length=1000),
        ),
    ]
