# Generated by Django 4.2.5 on 2024-05-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_finder_app', '0011_delete_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ubisoft',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]