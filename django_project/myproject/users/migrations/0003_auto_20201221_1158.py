# Generated by Django 3.1.4 on 2020-12-21 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201221_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adduser',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]