# Generated by Django 4.2.6 on 2023-10-20 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_gym_table_alter_trainer_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='client',
            table='api_client',
        ),
    ]
