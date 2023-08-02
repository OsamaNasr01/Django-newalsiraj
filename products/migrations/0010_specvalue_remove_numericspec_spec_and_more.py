# Generated by Django 4.2.3 on 2023-08-02 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_spec_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.FloatField()),
                ('text', models.CharField(max_length=100)),
                ('bo', models.BooleanField()),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numeric', to='products.spec')),
            ],
        ),
        migrations.RemoveField(
            model_name='numericspec',
            name='spec',
        ),
        migrations.RemoveField(
            model_name='textspec',
            name='spec',
        ),
        migrations.DeleteModel(
            name='BooleanSpec',
        ),
        migrations.DeleteModel(
            name='NumericSpec',
        ),
        migrations.DeleteModel(
            name='TextSpec',
        ),
    ]