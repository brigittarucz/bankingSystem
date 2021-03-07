# Generated by Django 3.1.7 on 2021-03-07 10:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_app', '0003_auto_20210307_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='id',
            field=models.AutoField(auto_created=True, default=123123, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
