# Generated by Django 2.0.5 on 2019-07-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In progress'), ('successeded', 'Successeded'), ('failed', 'Failed')], default='pending', max_length=10)),
                ('result', models.TextField(null=True)),
            ],
        ),
    ]