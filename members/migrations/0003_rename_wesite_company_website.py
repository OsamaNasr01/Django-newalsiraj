# Generated by Django 4.2.3 on 2023-07-25 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_company_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='wesite',
            new_name='website',
        ),
    ]
