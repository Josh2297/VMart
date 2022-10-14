# Generated by Django 4.0.5 on 2022-10-03 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_alter_customuser_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='region_of_del',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state_of_origin',
            field=models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Abuja Federal Capital Territory', 'Abuja Federal Capital Territory'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Katsina State', 'Katsina State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('State', 'State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State')], help_text='Optional', max_length=50, null=True, verbose_name='State of Origin'),
        ),
    ]
