# Generated by Django 3.1.2 on 2020-10-13 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20201013_1230'),
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
