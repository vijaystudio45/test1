# Generated by Django 3.2.10 on 2021-12-08 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0002_alter_test_allowed_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test_allowed',
            new_name='dbFileds',
        ),
        migrations.AlterModelTable(
            name='dbfileds',
            table='allowed_fields',
        ),
    ]
