# Generated by Django 3.1.4 on 2020-12-28 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201228_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='logo',
            field=models.ImageField(default='null', upload_to=''),
            preserve_default=False,
        ),
    ]