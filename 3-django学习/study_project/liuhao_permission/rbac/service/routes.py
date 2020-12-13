from collections import OrderedDict
from django.conf import settings
from django.utils.module_loading import import_string  # 功能是根据字符串的形式导入模块
from django.urls import resolvers
import re


def check_url_exclude(url):
    """
    排除一些url
    :param url:
    :return:
    """
    exclude_url = settings.AUTO_DISCOVER_EXCLUDE
    for regex in exclude_url:
        if re.search(regex, url):
            return True


def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
    """
    用于递归循环处理所有的url
    :param pre_namespace:namespace的前缀，用于拼接name    'rbac:menu_list'
    :param pre_url: 要拼接的url的前缀，用于生成正确的url  /rbac/menu/list
    :param urlpatterns:就是路由关系   /menu/list
    :param url_ordered_dict:用于保存递归中的所有路由
    得到的路由以下面的形式进行保存
    {
        'rbac:menu_list': {name:'rbac:menu_list', url:xxx/xxx/menu/list/}
    }
    :return:
    """
    for item in urlpatterns:
        if isinstance(item, resolvers.URLPattern):  # 是非路由分发的类型，将路由添加到字典url_ordered_dict中
            if not item.name:
                continue
            name = item.name
            if pre_namespace:
                name = '%s:%s' % (pre_namespace, item.name)
                name = name.replace('admin:', '')
            url = '%s%s' % (pre_url, item.pattern)
            new_url = url.replace('/^admin', '').replace('^', '').replace('$', '')
            if check_url_exclude(url):
                continue
            url_ordered_dict[name] = {'name': name, 'url': new_url}
        elif isinstance(item, resolvers.URLResolver):
            if pre_namespace:
                if item.namespace:
                    pre_namespace = '%s:%s' % (pre_namespace, item.namespace)
                else:
                    pre_namespace = pre_namespace
            else:
                if item.namespace:
                    pre_namespace = item.namespace
                else:
                    pre_namespace = None
            pre_url = '%s%s' % (pre_url, item.pattern)
            recursion_urls(pre_namespace, pre_url, item.url_patterns, url_ordered_dict)


def get_all_url_dict():
    """
    获取到全部的url
    :return:
    """
    url_ordered_dict = OrderedDict()
    md = import_string(settings.ROOT_URLCONF)
    recursion_urls(None, '/', md.urlpatterns, url_ordered_dict)  # 递归的获取所有的路由
    return url_ordered_dict
