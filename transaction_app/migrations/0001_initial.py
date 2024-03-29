# Generated by Django 3.1.7 on 2021-04-01 13:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts_app_account', '0001_initial'),
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_account_number_sender', models.CharField(max_length=20)),
                ('transaction_account_number_receiver', models.CharField(max_length=20)),
                ('transaction_id', models.CharField(max_length=20)),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(5.0)])),
                ('transaction_currency', models.CharField(max_length=3)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_user_account_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts_app_account.account')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.CharField(max_length=20)),
                ('loan_description', models.CharField(max_length=20)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(5.0)])),
                ('loan_date', models.DateTimeField(auto_now_add=True)),
                ('loan_remain', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(5.0)])),
                ('loan_account_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth_app.profile')),
            ],
        ),
    ]
