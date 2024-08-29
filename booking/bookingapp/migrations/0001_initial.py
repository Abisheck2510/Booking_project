# Generated by Django 5.0.6 on 2024-08-08 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default=None, max_length=20)),
                ('phone_number', models.IntegerField()),
                ('pickup_point', models.CharField(max_length=30)),
                ('drop_point', models.CharField(max_length=30)),
                ('service_class', models.CharField(choices=[('seater', 'Seater'), ('semi-sleeper', 'Semi-Sleeper'), ('sleeper', 'Sleeper')], default='economy', max_length=20)),
            ],
        ),
    ]
