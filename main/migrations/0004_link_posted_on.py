# Generated by Django 3.1.4 on 2020-12-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_link_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='posted_on',
            field=models.DateField(auto_now=True),
        ),
    ]
