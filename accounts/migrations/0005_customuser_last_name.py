# Generated by Django 5.2.4 on 2025-07-21 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_is_active_customuser_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, null=True),
        ),
    ]
