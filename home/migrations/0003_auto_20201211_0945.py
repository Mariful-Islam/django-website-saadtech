# Generated by Django 3.1 on 2020-12-11 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='booktitle',
            field=models.CharField(max_length=500),
        ),
    ]