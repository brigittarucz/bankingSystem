# Generated by Django 3.1.6 on 2021-05-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='customer_rank',
            field=models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver'), ('bronze', 'Bronze')], default='bronze', max_length=10),
        ),
    ]
