# Generated by Django 3.2.1 on 2022-07-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_payment_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
