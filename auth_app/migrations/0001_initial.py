# Generated by Django 3.1.6 on 2021-03-03 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_rank', models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver'), ('bronze', 'Bronze')], max_length=10)),
                ('customer_phone_number', models.CharField(max_length=20)),
                ('customer_token', models.CharField(max_length=256)),
                ('customer_multi_factor_enabled', models.BooleanField()),
                ('customer_can_make_loans', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
