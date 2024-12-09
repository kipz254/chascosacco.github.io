# Generated by Django 5.1.3 on 2024-12-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('zone', models.CharField(max_length=25)),
            ],
        ),
    ]
