# Generated by Django 4.1.7 on 2023-03-08 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0001_initial'),
        ('rental_app', '0003_rental_video_video_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='MEM_NUM',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='member_app.memberprofile'),
        ),
    ]