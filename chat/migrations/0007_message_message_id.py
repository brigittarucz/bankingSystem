# Generated by Django 3.2.3 on 2021-05-25 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_message_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
