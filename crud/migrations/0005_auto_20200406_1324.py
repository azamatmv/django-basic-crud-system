# Generated by Django 3.0.4 on 2020-04-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20200406_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
