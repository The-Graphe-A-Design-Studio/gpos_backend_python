# Generated by Django 4.1.7 on 2023-04-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0076_transactiondetailsmaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactiondetailsmaster',
            name='mop',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='transactiondetailsmaster',
            name='products',
            field=models.JSONField(),
        ),
    ]
