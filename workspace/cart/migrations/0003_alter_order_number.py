# Generated by Django 4.1.3 on 2022-12-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(max_length=32),
        ),
    ]
