# Generated by Django 3.2.22 on 2023-12-12 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('home', '0057_solutionpage_meta_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryFormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Oddaja najemniške izkušnje',
                'verbose_name_plural': 'Oddaja najemniške izkušnje',
            },
            bases=('wagtailcore.page',),
        ),
    ]