# Generated by Django 4.0.6 on 2022-07-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(default=1, max_length=30),
        ),
    ]
