# Generated by Django 3.0.7 on 2020-07-12 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_auto_20200712_0327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='lang',
            new_name='Language',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='pages',
            new_name='Pages',
        ),
    ]
