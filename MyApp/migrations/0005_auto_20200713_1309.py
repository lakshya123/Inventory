# Generated by Django 3.0.7 on 2020-07-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_auto_20200713_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Subject',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='Title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
