# Generated by Django 4.0.4 on 2022-05-13 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_rename_assigned_order_courier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment',
            new_name='payed',
        ),
    ]
