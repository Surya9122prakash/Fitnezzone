# Generated by Django 3.0.14 on 2022-05-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_column='Email', max_length=254, primary_key=True, serialize=False),
        ),
    ]
