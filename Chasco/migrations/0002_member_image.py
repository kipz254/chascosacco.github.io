# Generated by Django 5.1.3 on 2024-12-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chasco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, upload_to='Member_images/'),
        ),
    ]
