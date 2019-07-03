# Generated by Django 2.2.2 on 2019-07-03 15:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=256)),
                ('open_from', models.CharField(max_length=10)),
                ('open_to', models.CharField(max_length=10)),
                ('published', models.BooleanField(default=False)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('sunday', models.BooleanField()),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('snap', models.BooleanField()),
                ('wic', models.BooleanField()),
                ('fmnp', models.BooleanField()),
                ('fresh_produce', models.BooleanField()),
                ('mrfei_score', models.IntegerField()),
                ('food_bucks', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=256)),
                ('street_one', models.CharField(max_length=256)),
                ('street_two', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
                ('zip_code', models.CharField(max_length=256)),
                ('location_description', models.TextField()),
                ('latitude', models.BooleanField()),
                ('longitude', models.BooleanField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
