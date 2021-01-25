from django.template import Library
from django.conf import settings
import re
from collections import OrderedDict
from django.urls import reverse
from django.http import QueryDict

register = Library()


@register.inclusion_tag('static_menu.html')
def static_menu(request):
    """
    创建一级菜单， inclusion_tag的作用是主动渲染
    :return:
    """
    menu_list = request.session.get(settings.MENU_SESSION_KEY)
    current_url = request.path_info
    active = None
    for url in menu_list:
        reg = '^%s$' % url
        if re.match(reg, current_url):
            active = 'active'
    return {'menu_list': menu_list, 'active': active}


@register.inclusion_tag('multi_menu.html')
def multi_menu(request):
    """

    这是用来生成左边二级菜单的，如果选中了，如果二级菜单被选中就让它展示出来
    :param request:
    :return:
    """
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)
    current_selected_permission = request.current_selected_permission
    # 对字典的key进行排序
    key_list = sorted(menu_dict)
    # 创建一个空的有序字典
    ordered_dict = OrderedDict()
    # 根据排序完的key从menus中取值
    for key in key_list:
        val = menu_dict[key]
        # 给每一个一级标题增加一个hide属性，默认设置为隐藏
        val['class'] = 'hide'
        for per in val['children']:
            # 只要当前url的id和请求里面的id，不管是id，还是pid，只要相同我们就让它被选中
            # 因为当是id的时候，它就应该被选中
            # 当是pid的时候，说明，是在它的内部做的操作，应该隶属于它
            if per['id'] == current_selected_permission:
                # 增加选中属性
                per['class'] = 'active'
                # 当被选中时对样式
                per['style'] = 'background:pink'
                # 同时去除一级标题的隐藏
                val['class'] = ''
            ordered_dict[key] = val
    return {'menu_dict': ordered_dict}


@register.inclusion_tag('breadcrumb.html')
def breadcrumb(request):
    """
    用来做导航条的
    :param request:
    :return:
    """
    return {'record_list': request.url_record}


@register.filter
def has_permission(request, name):
    """
    用来判断是否有权限,用来做权限的粒度控制，有权限就就让这个按钮显示出来，没有权限，就不让他做显示
    filter函数可以用来做判断的条件
    :param request:请求相关的所有信息
    :param name:url的别名
    :return:
    """
    if name in request.session.get(settings.PERMISSION_SESSION_KEY):
        return True


@register.simple_tag
def memory_url(request, name, *args, **kwargs):
    """
    自定义一个带原搜索条件的url，将？后面的条件给它进行保存起来，便于反向生成返回的时候能够操持原来的条件不变
    :param request: 请求相关的信息
    :param name: 将要跳转的url
    :param args: 传递过来的参数，以元组的形式保存的
    :param kwargs: 传递过来的参数以字典的形式保存的
    :return: 返回一个带有原条件的url
    """
    basic_url = reverse(name, args=args, kwargs=kwargs)
    if not request.GET:
        return basic_url
    query_dict = QueryDict(mutable=True)
    # 拿到原有的条件放到一个字典中， 后面再从字典中拿取出来用于反向生成
    query_dict['_filter'] = request.GET.urlencode()
    return '%s?%s' % (basic_url, query_dict.urlencode())
