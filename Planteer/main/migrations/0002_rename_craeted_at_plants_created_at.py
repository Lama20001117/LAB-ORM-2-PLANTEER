# Generated by Django 5.0.2 on 2024-03-21 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plants',
            old_name='craeted_at',
            new_name='created_at',
        ),
    ]
