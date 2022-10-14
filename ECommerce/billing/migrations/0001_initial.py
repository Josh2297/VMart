# Generated by Django 4.0.5 on 2022-10-03 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('txn_id', models.ForeignKey(help_text='Transaction ID is the unique code that Can Be Used To Track the status of an Order', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='order.order')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('phone_no', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('delivery_method', models.CharField(choices=[('home_delivery', 'Home Delivery'), ('pick_up_station', 'Pick Up Station')], default='home_delivery', max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(help_text='Enter Shipping Address', max_length=50, verbose_name='Delivery Address')),
                ('total', models.IntegerField(help_text='Total Sum is in Naira', verbose_name='Total Sum')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
