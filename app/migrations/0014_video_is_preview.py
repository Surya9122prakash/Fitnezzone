# Generated by Django 4.0.4 on 2022-05-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_usercourse_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='is_preview',
            field=models.BooleanField(default=False),
        ),
    ]
