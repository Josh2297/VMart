# Generated by Django 4.0.5 on 2022-10-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='occupation',
        ),
        migrations.AddField(
            model_name='customuser',
            name='addional_phone_no',
            field=models.CharField(blank=True, help_text='Add an additional Phone Number (Optional)', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='services',
            field=models.CharField(blank=True, help_text='What Services do you intend to offer Play?', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='home_address',
            field=models.CharField(blank=True, help_text='Home Address is Optional', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='location_of_del',
            field=models.CharField(blank=True, help_text='This Location can be changed for Every Order Made', max_length=20, null=True, verbose_name='Preferred Location of Delivery'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.IntegerField(verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images', verbose_name='Upload a Profile Picture'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='region_of_del',
            field=models.CharField(blank=True, help_text='This Region can be changed for Every Order Made', max_length=20, null=True, verbose_name='Preferred Region of Delivery'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state_of_origin',
            field=models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Abuja Federal Capital Territory', 'Abuja Federal Capital Territory'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Katsina State', 'Katsina State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('State', 'State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State')], max_length=50, null=True, verbose_name='State of Origin'),
        ),
    ]
