# Generated by Django 4.1.3 on 2024-01-01 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='descProduct',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='imageProduct',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ukuran',
            new_name='sizeProduct',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stok',
            new_name='stockProduct',
        ),
    ]
