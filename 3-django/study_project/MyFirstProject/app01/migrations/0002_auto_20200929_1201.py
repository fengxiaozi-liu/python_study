# Generated by Django 3.1.1 on 2020-09-29 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachertoclass',
            name='cles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cles_id', to='app01.classes'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
