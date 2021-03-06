# Generated by Django 3.0.7 on 2020-07-13 06:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_auto_20200712_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Pages',
        ),
        migrations.AddField(
            model_name='book',
            name='Author',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='Stock',
            field=models.IntegerField(blank=True, default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='TimeStamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='book',
            name='Language',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='Subject',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='Title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
