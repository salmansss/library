# Generated by Django 4.0.6 on 2022-07-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=255)),
                ('cat_slug', models.CharField(max_length=255)),
                ('status', models.CharField(default=0, max_length=30)),
            ],
        ),
    ]
