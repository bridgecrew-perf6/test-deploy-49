# Generated by Django 4.0.3 on 2022-03-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
        ('account', '0003_alter_profile_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to='movie.movie'),
        ),
    ]
