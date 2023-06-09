# Generated by Django 4.1.7 on 2023-04-17 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0106_remove_purchasetransactiondetails_related_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesregister',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='salesregister',
            name='row_total',
        ),
        migrations.AddField(
            model_name='barcode',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='barcode', to='POSDemo.product'),
        ),
        migrations.AddField(
            model_name='barcode',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='barcode', to='POSDemo.storemaster'),
        ),
        migrations.CreateModel(
            name='InventoryManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField()),
                ('action', models.CharField(choices=[('A', 'added'), ('R', 'removed')], max_length=1)),
                ('quantiy', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventorymanager', to='POSDemo.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventorymanager', to='POSDemo.storemaster')),
            ],
        ),
    ]
