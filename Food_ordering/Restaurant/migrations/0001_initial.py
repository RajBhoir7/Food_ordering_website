# Generated by Django 4.2.3 on 2023-08-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rest_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rest_name', models.CharField(max_length=50)),
                ('Owner_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Owner_contact', models.BigIntegerField()),
                ('Rest_location', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
