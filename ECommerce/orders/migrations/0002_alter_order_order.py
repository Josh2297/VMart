# Generated by Django 4.0.5 on 2022-09-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.CharField(max_length=9999, verbose_name='List of Orders'),
        ),
    ]
