# Generated by Django 3.0.3 on 2020-03-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_num',
            field=models.IntegerField(help_text='Please enter your customer code'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fullname',
            field=models.CharField(help_text='Please enter your name', max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(help_text='Please enter your mobile num '),
        ),
    ]
