# Generated by Django 3.1.7 on 2021-03-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.IntegerField(choices=[("Didn't start", "Didn't start"), ('Start', 'Start'), ('Ended', 'Ended')], default=0),
        ),
    ]
