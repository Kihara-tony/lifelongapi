# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-24 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0002_auto_20190924_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.CharField(choices=[('Bars', 'bars'), ('Restaurants ', 'restaurants'), ('Botique', 'botique'), ('Foods', 'foods'), ('Supermarkets', 'supermarkets'), ('Bookshop', 'bookshop'), ('Hospitals', 'hospitals'), ('Electric Hardware', 'electric hardware'), ('Construction Material Hardware', 'construction material hardware')], default='Hotel', max_length=100),
        ),
        migrations.AlterField(
            model_name='business',
            name='status',
            field=models.CharField(choices=[('For Sale', 'For Sale'), ('In Business', 'In business')], default='for rent', max_length=50),
        ),
        migrations.AlterField(
            model_name='housing',
            name='amenities',
            field=models.CharField(choices=[('Security', 'Security'), ('Electricity', 'Electricity'), (' Good Road', 'Good Road'), ('School', 'School'), ('Hospital', 'Hospital'), ('Water', 'Water')], default='security', max_length=50),
        ),
        migrations.AlterField(
            model_name='housing',
            name='category',
            field=models.CharField(choices=[('Rooms', 'rooms'), ('Container Houses', 'container houses'), ('Mansionette', 'mansionette'), ('Hostels', 'hostels'), ('Bungalows', 'bungalows'), ('Studio ', 'studio'), ('Flats and Apartments', 'flats and apartments'), ('Town Houses', 'town houses'), ('Bedsitters', 'bedsitters'), ('Single Rooms', 'single rooms'), ('Houses', 'houses')], default='appartment', max_length=100),
        ),
        migrations.AlterField(
            model_name='housing',
            name='mode_of_payment',
            field=models.CharField(choices=[('M-pesa', 'M-pesa'), ('Paypal', 'Paypal')], default='m-pesa', max_length=50),
        ),
        migrations.AlterField(
            model_name='housing',
            name='status',
            field=models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='for rent', max_length=50),
        ),
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.CharField(choices=[('Massage', 'massage'), ('Shoe repair', 'shoe repair'), ('Plumber', 'plumber'), ('Fencing service', 'fencing service'), ('Library', 'library'), ('Vehicle Branding', 'vehicle branding'), ('Water point', 'water point'), ('Car Tracking', 'car tracking'), ('Electrician', 'Electrician'), ('House maid service', 'house maid service'), ('Photographer', 'photographer'), ('Barber', 'barber'), ('Swimming Pool maintenance', 'swimming pool maintenance'), ('Phone repair', 'phone repair'), ('Spa', 'spa'), ('Lawyers', 'lawyers'), ('Church,Mosque', 'church,mosque'), ('Gardener', 'gardener'), ('Security Guard', 'security guard'), ('Saloon', 'saloon'), ('Cyber', 'cyber'), ('T-shirt Printing', 'T-shirt Printing'), ('Kibanda foods', 'kibanda foods')], default='plumber', max_length=100),
        ),
        migrations.AlterField(
            model_name='services',
            name='status',
            field=models.CharField(choices=[('For Sale', 'For Sale'), ('In Business', 'In business')], default='for rent', max_length=50),
        ),
    ]
