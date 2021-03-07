# Generated by Django 3.1.7 on 2021-03-07 10:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_app', '0002_auto_20210306_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='id',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
