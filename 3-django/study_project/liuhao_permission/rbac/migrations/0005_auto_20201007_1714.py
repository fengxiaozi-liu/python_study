# Generated by Django 3.1.2 on 2020-10-07 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='is_menu',
        ),
        migrations.AddField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(blank=True, help_text='null表示不是菜单，非null表示是二级菜单', null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.menu', verbose_name='所属一级菜单'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='icon',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='一级菜单图标'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=32, verbose_name='一级菜单'),
        ),
    ]
