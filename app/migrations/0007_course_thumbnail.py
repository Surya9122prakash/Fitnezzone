# Generated by Django 4.0.4 on 2022-05-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_course_days_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='files/thumbnail'),
        ),
    ]
