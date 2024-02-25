# Generated by Django 4.2.9 on 2024-02-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_productimages_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_choice',
        ),
        migrations.AddField(
            model_name='product',
            name='life',
            field=models.CharField(blank=True, default='2 days', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_count',
            field=models.CharField(blank=True, choices=[('draft', 'Draft'), ('deliver', 'Delivered'), ('rejected', 'Rejected'), ('in_review', 'In Review'), ('published', 'Published')], default='1', max_length=10),
        ),
    ]