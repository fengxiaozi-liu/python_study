# Generated by Django 3.1.1 on 2020-09-20 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_boy_m'),
    ]

    operations = [
        migrations.AddField(
            model_name='love',
            name='time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='love',
            unique_together=set(),
        ),
    ]
