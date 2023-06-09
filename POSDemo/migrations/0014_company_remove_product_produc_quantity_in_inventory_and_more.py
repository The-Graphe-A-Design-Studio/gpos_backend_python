# Generated by Django 4.1.7 on 2023-03-21 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0013_rename_inventory_productinventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='produc_quantity_in_inventory',
        ),
        migrations.AddField(
            model_name='product',
            name='product_quantity_in_inventory',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='POSDemo.productinventory'),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='POSDemo.company')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='POSDemo.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='POSDemo.company'),
        ),
    ]
