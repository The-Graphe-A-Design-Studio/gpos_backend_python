# Generated by Django 4.1.7 on 2023-03-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0027_alter_business_business_pan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='contact_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='owner',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
