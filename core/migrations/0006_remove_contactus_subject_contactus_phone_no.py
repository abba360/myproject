# Generated by Django 4.2.9 on 2024-02-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_contactus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='Subject',
        ),
        migrations.AddField(
            model_name='contactus',
            name='phone_no',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]