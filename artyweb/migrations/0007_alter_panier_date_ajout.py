# Generated by Django 4.2.1 on 2023-05-15 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('artyweb', '0006_alter_panier_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panier',
            name='date_ajout',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
