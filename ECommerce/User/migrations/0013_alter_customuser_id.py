# Generated by Django 4.0.5 on 2022-10-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.CharField(default='3533bf2d6a3b902f', max_length=50, primary_key=True, serialize=False),
        ),
    ]