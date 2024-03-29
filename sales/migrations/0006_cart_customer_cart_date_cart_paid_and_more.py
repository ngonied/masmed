# Generated by Django 4.0.4 on 2022-05-10 14:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('sales', '0005_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='pay_on_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='pescription',
            field=models.FileField(null=True, upload_to='files/pescriptions'),
        ),
    ]
