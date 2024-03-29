# Generated by Django 4.2.9 on 2024-02-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_user_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('Subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
