# Generated by Django 3.0.4 on 2020-04-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getimg', '0009_auto_20200324_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='name', max_length=30),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]