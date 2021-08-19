# Generated by Django 3.2.6 on 2021-08-16 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20210816_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproblem',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Pregledano s strani administratorja'),
        ),
        migrations.AlterField(
            model_name='solutionpage',
            name='user_problem',
            field=models.ForeignKey(limit_choices_to={'approved': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.userproblem', verbose_name='Uporabniški problem'),
        ),
    ]