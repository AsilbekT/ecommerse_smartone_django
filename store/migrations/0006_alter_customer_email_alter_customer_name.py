# Generated by Django 4.0 on 2021-12-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
    ]
