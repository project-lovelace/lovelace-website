# Generated by Django 2.1.2 on 2018-10-26 21:00

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_added_date_format_help_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='/static/img/default_avatar.png', upload_to=users.models.avatar_file_name),
        ),
    ]