# Generated by Django 2.2.13 on 2021-04-02 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.IntegerField(default=20),
        ),
    ]