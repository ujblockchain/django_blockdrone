# Generated by Django 5.0.2 on 2024-04-23 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_page', '0010_jobrequestmodel_request_tel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobrequestmodel',
            name='request_address',
        ),
        migrations.AddField(
            model_name='jobrequestmodel',
            name='request_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drone_page.city'),
        ),
        migrations.AddField(
            model_name='jobrequestmodel',
            name='request_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drone_page.country'),
        ),
    ]
