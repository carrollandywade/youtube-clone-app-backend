# Generated by Django 3.1.8 on 2021-07-22 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_Id', models.CharField(max_length=100)),
                ('comment_to_video', models.CharField(max_length=100)),
                ('like_video', models.IntegerField(default=0)),
                ('dislike_video', models.IntegerField(default=0)),
            ],
        ),
    ]
