# Generated by Django 4.1.7 on 2023-04-03 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0063_alter_auth_token_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='token_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
