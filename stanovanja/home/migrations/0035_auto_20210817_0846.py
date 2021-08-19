# Generated by Django 3.2.6 on 2021-08-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20210816_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalstory',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Zemljepisna širina'),
        ),
        migrations.AddField(
            model_name='rentalstory',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Zemljepisna dolžina'),
        ),
    ]