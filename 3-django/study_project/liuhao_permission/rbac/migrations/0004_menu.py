# Generated by Django 3.1.2 on 2020-10-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_permission_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('icon', models.CharField(blank=True, max_length=32, null=True, verbose_name='图标')),
            ],
        ),
    ]
