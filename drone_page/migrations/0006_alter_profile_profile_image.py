# Generated by Django 5.0.2 on 2024-04-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_page', '0005_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
