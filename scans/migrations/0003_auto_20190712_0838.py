# Generated by Django 2.0.5 on 2019-07-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0002_auto_20190711_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In progress'), ('successeded', 'Successeded'), ('failed', 'Failed')], default='pending', max_length=15),
        ),
    ]
