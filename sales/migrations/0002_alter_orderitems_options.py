# Generated by Django 4.0.4 on 2022-05-07 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitems',
            options={'verbose_name_plural': 'Order Items'},
        ),
    ]