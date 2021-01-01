# Generated by Django 3.1 on 2020-11-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookcover', models.ImageField(upload_to='media')),
                ('bookfile', models.FileField(upload_to='media')),
                ('booktitle', models.CharField(max_length=200)),
            ],
        ),
    ]
