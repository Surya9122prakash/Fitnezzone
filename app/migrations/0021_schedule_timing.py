# Generated by Django 4.0.4 on 2022-05-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_schedule_mail_id_alter_schedule_ph_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='timing',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
