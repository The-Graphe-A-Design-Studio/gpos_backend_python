# Generated by Django 4.1.7 on 2023-04-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0100_daily_employee_management'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseregister',
            name='total',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
