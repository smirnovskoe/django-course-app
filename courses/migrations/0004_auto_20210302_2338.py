# Generated by Django 3.1.7 on 2021-03-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210302_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('DIDNT', "Didn't start"), ('START', 'Start'), ('END', 'Ended')], default='DIDNT', max_length=20),
        ),
    ]
