# Generated by Django 3.0.3 on 2020-03-08 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_register', '0002_auto_20200309_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_num',
            new_name='customer_id',
        ),
    ]