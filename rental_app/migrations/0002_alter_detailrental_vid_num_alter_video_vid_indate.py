# Generated by Django 4.1.7 on 2023-02-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailrental',
            name='VID_NUM',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='VID_INDATE',
            field=models.DateField(null=True),
        ),
    ]
