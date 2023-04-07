# Generated by Django 4.1.7 on 2023-04-07 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0081_salesreturnregister'),
    ]

    operations = [
        migrations.RenameField(
            model_name='returnsalespending',
            old_name='bill_id',
            new_name='bill_ID',
        ),
        migrations.AddField(
            model_name='returnsalespending',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='returnsalespending', to='POSDemo.employeemaster'),
        ),
    ]
