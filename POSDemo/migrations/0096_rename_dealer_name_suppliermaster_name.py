# Generated by Django 4.1.7 on 2023-04-12 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0095_suppliermaster_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suppliermaster',
            old_name='dealer_name',
            new_name='name',
        ),
    ]
