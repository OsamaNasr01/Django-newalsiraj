# Generated by Django 4.2.3 on 2023-07-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_created_at_alter_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(auto_created=True, null=True, unique=True),
        ),
    ]