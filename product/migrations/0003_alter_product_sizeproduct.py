# Generated by Django 4.1.3 on 2024-01-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_desc_product_descproduct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizeProduct',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=2),
        ),
    ]
