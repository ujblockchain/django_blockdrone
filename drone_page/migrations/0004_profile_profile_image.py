# Generated by Django 5.0.2 on 2024-04-19 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_page', '0003_remove_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
