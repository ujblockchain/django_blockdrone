# Generated by Django 5.0.2 on 2024-05-02 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(0, 'What role are you?'), (1, 'Client'), (2, 'Pilot')], help_text='What role are you?', max_length=25),
        ),
    ]
