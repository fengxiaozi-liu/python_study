from django.db import models


class Menu(models.Model):
    title = models.CharField(verbose_name='一级菜单', max_length=32)
    icon = models.CharField(verbose_name='一级菜单图标', max_length=32)

    def __str__(self):
        return self.title


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)
    name = models.CharField(max_length=16, verbose_name='url别名', unique=True, blank=True)
    # is_menu = models.BooleanField(verbose_name='是否可以做菜单', default=False)
    # icon = models.CharField(verbose_name='图标', max_length=32, null=True, blank=True)
    menu = models.ForeignKey(verbose_name='所属一级菜单',
                             null=True,
                             blank=True,
                             to='Menu',
                             help_text='null表示不是菜单，非null表示是二级菜单',
                             on_delete=models.CASCADE
                             )
    pid = models.ForeignKey(verbose_name='关联的权限',
                            help_text='对于一个非菜单的权限需要选择一个可以成为菜单的权限，用户做默认展开',
                            to='Permission',
                            null=True,
                            blank=True,
                            related_name='patents',
                            on_delete=models.CASCADE,
                            )

    def __str__(self):
        return self.title
