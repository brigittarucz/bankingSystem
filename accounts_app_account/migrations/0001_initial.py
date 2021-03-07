# Generated by Django 3.1.7 on 2021-03-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_user_fk', models.IntegerField()),
                ('account_number', models.CharField(max_length=20)),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
