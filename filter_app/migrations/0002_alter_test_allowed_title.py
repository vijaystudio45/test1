# Generated by Django 3.2.10 on 2021-12-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_allowed',
            name='title',
            field=models.CharField(max_length=500, null=True),
        ),
    ]