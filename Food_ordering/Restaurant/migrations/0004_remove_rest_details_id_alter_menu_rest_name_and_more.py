# Generated by Django 4.2.2 on 2023-09-08 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0003_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rest_details',
            name='id',
        ),
        migrations.AlterField(
            model_name='menu',
            name='Rest_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Restaurant.rest_details'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rest_details',
            name='Rest_name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
