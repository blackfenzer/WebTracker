# Generated by Django 5.1.5 on 2025-02-04 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_tracker', '0006_remove_trackeditem_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemresult',
            name='lowest_price',
        ),
    ]
