# Generated by Django 4.1.7 on 2023-04-13 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0102_purchaseregister_purchase_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasepending',
            old_name='product',
            new_name='purchase_rate',
        ),
        migrations.RenameField(
            model_name='purchasepending',
            old_name='product_quantity',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='purchasepending',
            name='date',
        ),
        migrations.RemoveField(
            model_name='purchasepending',
            name='quantity_type',
        ),
        migrations.AddField(
            model_name='purchasepending',
            name='date_and_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='purchasepending',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchasepending', to='POSDemo.product'),
        ),
        migrations.AddField(
            model_name='purchasepending',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchasepending', to='POSDemo.storemaster'),
        ),
        migrations.AddField(
            model_name='purchasepending',
            name='total',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
