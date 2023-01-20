# Generated by Django 4.1.5 on 2023-01-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('owner_contact', models.CharField(max_length=100)),
                ('owner_whatsapp', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('area', models.IntegerField()),
                ('image', models.ImageField(upload_to='gallery')),
                ('has_lights', models.BooleanField(default=False)),
                ('has_drinks', models.BooleanField(default=False)),
                ('has_sport_equipment', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]
