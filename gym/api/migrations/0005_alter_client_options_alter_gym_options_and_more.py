# Generated by Django 4.2.6 on 2023-10-20 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_client_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'managed': False, 'verbose_name_plural': 'Client'},
        ),
        migrations.AlterModelOptions(
            name='gym',
            options={'managed': False, 'verbose_name_plural': 'Gym'},
        ),
        migrations.AlterModelOptions(
            name='trainer',
            options={'managed': False, 'verbose_name_plural': 'Trainer'},
        ),
        migrations.AlterModelOptions(
            name='workoutsession',
            options={'managed': False, 'verbose_name_plural': 'WorkoutSession'},
        ),
    ]
