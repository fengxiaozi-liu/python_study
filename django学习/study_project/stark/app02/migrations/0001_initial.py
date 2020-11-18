# Generated by Django 3.1.2 on 2020-10-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=32, verbose_name='主机名')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
            ],
        ),
    ]
