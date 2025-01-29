# Generated by Django 5.1.4 on 2025-01-16 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('contact_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('def_name', models.CharField(max_length=100)),
                ('def_display_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_department', models.CharField(max_length=100)),
                ('doc_image', models.ImageField(upload_to='images/')),
                ('doc_description', models.TextField()),
                ('doc_specialization', models.TextField()),
                ('doc_experience', models.IntegerField()),
                ('doc_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=255)),
                ('p_phone', models.CharField(max_length=10)),
                ('p_email', models.EmailField(max_length=254)),
                ('booking_date', models.DateField()),
                ('booking_on', models.DateField(auto_now=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.doctor')),
            ],
        ),
    ]
