# Generated by Django 3.1.6 on 2021-04-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210428_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='currency_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='rate_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]