# Generated by Django 4.0.3 on 2022-03-23 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_favorite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]