# Generated by Django 5.1.6 on 2025-02-22 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='counters', to='frontend.user'),
        ),
    ]
