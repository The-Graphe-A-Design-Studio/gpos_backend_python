# Generated by Django 4.1.7 on 2023-04-12 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0096_rename_dealer_name_suppliermaster_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemaster',
            name='store',
        ),
        migrations.AddField(
            model_name='employeemaster',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee', to='POSDemo.business'),
        ),
    ]
