# Generated by Django 3.1.4 on 2021-01-06 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, unique=True)),
                ('carsName', models.CharField(default='', max_length=255, verbose_name='Cars name')),
                ('brand', models.CharField(default='', max_length=255, verbose_name='Brand name')),
                ('price', models.IntegerField()),
                ('color', models.CharField(default='', max_length=255, verbose_name='Color')),
                ('Carype', models.CharField(default='', max_length=255, verbose_name='Types')),
                ('plat', models.CharField(default='', max_length=10, verbose_name='Plat')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, unique=True)),
                ('firstName', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('lastName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rentDate', models.DateTimeField(null=True, verbose_name='Rent Date')),
                ('rentDateBack', models.DateTimeField(null=True, verbose_name='Rent Date Back')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updatedAt', models.DateTimeField(null=True, verbose_name='Updated At')),
                ('idCars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilmysql.cars')),
                ('idContacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilmysql.contact')),
            ],
        ),
    ]
