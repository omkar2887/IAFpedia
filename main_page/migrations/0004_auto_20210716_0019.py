# Generated by Django 3.1.4 on 2021-07-15 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_hisevent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HisEvent',
            new_name='HistoricalEvent',
        ),
    ]