# Generated by Django 3.0.4 on 2020-03-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getimg', '0008_auto_20200324_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(max_length=1000, upload_to='images/'),
        ),
    ]
