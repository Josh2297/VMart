# Generated by Django 4.0.5 on 2022-10-03 21:21

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
            name='Order',
            fields=[
                ('trxn_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Transaction ID')),
                ('date', models.DateTimeField(verbose_name='Date of Order')),
                ('order', models.CharField(max_length=10000, verbose_name='Order Items')),
                ('total', models.IntegerField(verbose_name='Total of Purchase')),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('not_payed', 'Not Payed'), ('failed', 'Failed'), ('successful', 'Successful')], default='pending', max_length=20)),
                ('delivery_status', models.CharField(choices=[('pending', 'Pending'), ('delivered', 'Delivered'), ('not_delivered', 'Not Delivered'), ('delivery_failed', 'Delivery Failed'), ('other', 'Other')], default='pending', max_length=20)),
                ('payment_id', models.CharField(blank=True, max_length=10, null=True)),
                ('first_six_digit', models.IntegerField(blank=True, null=True)),
                ('last_four_digit', models.IntegerField(blank=True, null=True)),
                ('charged_amount', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='Date and Time of Payment')),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
