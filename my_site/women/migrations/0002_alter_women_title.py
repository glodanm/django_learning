# Generated by Django 4.1.2 on 2022-11-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
