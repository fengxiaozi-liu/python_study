from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, render, HttpResponse
import re
from django.conf import settings


class RbacMiddleware(MiddlewareMixin):
    """
    用户权限信息的校验
    """

    def process_request(self, request):
        """
        用户请求进来的时候获取
        :param request:
        :return:
        """
        # 获取当前用户的url，获取当前用户在session中保存的权限列表
        # 最后完成权限信息的匹配
        current_url = request.path_info
        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
        # 白名单
        valid_url_list = settings.VALID_URL_LIST
        # 凡是在白名单里面的都不需要验证了，直接走后面的中间件
        for valid_url in valid_url_list:
            if re.search(valid_url, current_url):
                return None
        # 如果用户信息不存在则返回到登录页面
        if not permission_dict:
            return redirect('/login/')
        flag = False
        # 对传过来的权限做判断，是否可以做菜单默认选择
        url_record = [
            {'title': '首页', 'url': '#'}
        ]
        for item in permission_dict.values():
            reg = '^%s$' % item['url']
            if re.match(reg, current_url):
                flag = True
                # 将每一个url权限的id或者是pid放到请求里面，以供用于生成动态的菜单
                request.current_selected_permission = item['pid'] or item['id']
                if not item['pid']:
                    url_record.append({'title': item['title'], 'url': item['url'], 'class': 'active'})
                else:
                    url_record.extend([
                        {'title': item['p_title'], 'url': item['p_url']},
                        {'title': item['title'], 'url': item['url'], 'class': 'active'}]
                    )
                request.url_record = url_record
                break
        if not flag:
            return HttpResponse('您的权限不够，当前无法访问，您可以向上级申请权限')
