# Generated by Django 3.0.4 on 2020-04-06 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20200406_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
