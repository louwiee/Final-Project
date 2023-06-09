# Generated by Django 4.1.7 on 2023-03-08 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0002_alter_detailrental_vid_num_alter_video_vid_indate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='VIDEO',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rental_app.video'),
        ),
        migrations.AddField(
            model_name='video',
            name='MOVIE',
            field=models.ManyToManyField(to='rental_app.movie'),
        ),
    ]
