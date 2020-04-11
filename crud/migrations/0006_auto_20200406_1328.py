# Generated by Django 3.0.4 on 2020-04-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20200406_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.CharField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', max_length=200),
        ),
    ]
