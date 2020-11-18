from types import FunctionType
import functools
from django.http import QueryDict
from django.shortcuts import HttpResponse, render, redirect, reverse
from django.urls import re_path
from django.utils.safestring import mark_safe
from .pagination import Pagination
from django import forms


class StarkHandler:
    """
    对表进行操作的类,在这个类中进行编写视图函数，生成url 和对指定的url取名
    """

    def __init__(self, model_class, prev=None):
        """

        :param model_class: 要处理的指定表对应的类
        :param prev: 想要给对应的url生成name时的前缀
        """
        self.model_class = model_class
        self.prev = prev
        self.request = None

    # ==================================================为对应的url设置一个name===================================
    def set_urls_name(self, param):
        """
        根据app名称和表名称来生成url的name
        :param param: 传递进来的指定的name
        :return:
        """
        app_name = self.model_class._meta.app_label
        table_name = self.model_class._meta.model_name
        # 如果有前缀就加上前缀， 没有就不加前缀
        if self.prev:
            return '%s_%s_%s_%s' % (app_name, table_name, self.prev, param)
        else:
            return '%s_%s_%s' % (app_name, table_name, param)

    @property
    def get_list_name(self):
        """
        获取列表名称
        :return:
        """
        return self.set_urls_name('list')

    @property
    def get_add_name(self):
        """
        获取添加列表的名称
        :return:
        """
        return self.set_urls_name('add')

    @property
    def get_change_name(self):
        """
        获取编辑列表的名称
        :return:
        """
        return self.set_urls_name('change')

    @property
    def get_del_name(self):
        """
        获取删除列表的名称
        :return:
        """
        return self.set_urls_name('del')

    # ===========================================在列表页面上应该显示的字段==============================================

    # 想要显示的字段表格，可以在对应的Handler类中重写表格数据，教给get_display_list进行处理
    display_list = []  # 是想在列表页面显示的字段，可以自定制

    def get_display_list(self):
        """
        自定制display_list，拿到每一个表中对应的字段 可以去指定的Handler类里面重写get_display_list， 就能够再进行一步判断操作
        :return:
        """
        display_list = []
        display_list.extend(self.display_list)
        return display_list

    @staticmethod
    def get_choices_text(name, field):
        """
        自定制的拿出函数choice字段的文本名，让它显示在页面上
        :param name: 希望页面显示表头名
        :param field: 在数据库中的字段
        :return: 内部的inner函数
        """

        def inner(self, obj=None, is_header=None):
            if is_header:
                return name
            new_field = 'get_%s_display' % field
            return getattr(obj, new_field)()

        return inner

    # ===============================================保留原搜索条件反向生成url的函数=========================================

    # 保留原搜索条件的列表的url
    def reverse_list_url(self):
        name = '%s:%s' % (site.namespace, self.get_list_name)
        url = reverse(name)
        param = self.request.GET.get('_filter')
        if not param:
            list_url = url
        else:
            list_url = '%s?%s' % (url, param)
        return list_url

    def reverse_change_url(self, pk=None, name=None):
        name = '%s:%s' % (site.namespace, name)
        if not pk:
            url = reverse(name)
        else:
            url = reverse(name, args=(pk,))
        if not self.request.GET:
            origin_url = url
        else:
            query_dict = QueryDict(mutable=True)
            param = self.request.GET.urlencode()
            query_dict['_filter'] = param
            origin_url = '%s?%s' % (url, query_dict.urlencode())
        return origin_url

    # ========================================是否在列表页面上显示添加，编辑或者删除按钮========================================
    has_add_btn = True

    def get_add_btn(self):
        """
        预留的钩子函数用来判断，是否显示添加按钮
        :return:
        """
        add_url = self.reverse_change_url(name=self.get_add_name)

        if self.has_add_btn:
            return '<a href="%s" class="btn btn-primary">添加</a>' % add_url
        return None

    def display_edit(self, obj=None, is_header=None):
        """
        自定制编辑函数，是否在列表页面上显示编辑按钮
        :param obj: 将数据库中的每一个对象那个传入函数
        :param is_header: 用来判断是表头，还是表内的数据，根据不同的判断，返回不同的内容
        :return:返回一个编辑的a标签
        """

        if is_header:
            return '编辑'
        change_url = self.reverse_change_url(obj.id, self.get_change_name)
        return mark_safe('<a href="%s" class="fa fa-pencil" aria-hidden="true"></a>' % change_url)

    def display_del(self, obj=None, is_header=None):
        """
        自定制函数，是否在列表页面上显示删除按钮
        :param obj:
        :param is_header:
        :return:返回一个删除的a标签
        """
        if is_header:
            return '删除'
        del_url = self.reverse_change_url(obj.id, self.get_del_name)
        return mark_safe('<a href="%s" class="fa fa-trash" aria-hidden="true" style="color:red"></a>' % del_url)

    # =============================定制统一的Form类，用于做form表单的验证(同时可以自定制在编辑页面上的字段)========================
    fields = None  # 通过fields可以自定制想要的字段， 是在添加编辑和删除页面想要显示的字段

    def get_model_form(self):
        """
        可以自定义 相关的Handler类中可以自定义想要的字段， 要和下面的save(self, form, is_update=False)方法配合使用
        :return:
        """

        class DynamicModel(forms.ModelForm):
            class Meta:
                model = self.model_class
                if not self.fields:
                    fields = '__all__'
                else:
                    fields = self.fields

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for name, field in self.fields.items():
                    field.widget.attrs['class'] = 'form-control'

        return DynamicModel

    def save(self, form, is_update=False):
        """
        自定义的钩子函数，可用于自定义
        :param form: 传递进来的Form对象
        :param is_update: 是否要更新
        :return:
        """
        form.save()

    # ========================================对应的列表，添加，编辑和删除的视图函数===========================================

    per_page = 10  # 添加了一个分页的功能，每页显示多少条数据，写在外面是为了方便自定制

    def list_views(self, request):
        """
        列表的全部数据
        :param request: 请求相关的信息
        :return:
        """
        self.request = request

        # 导入写好的自定义分页
        # ============================================处理分页====================================
        numbers = self.model_class.objects.all().count()
        query_params = request.GET.copy()
        query_params._mutable = True
        pager = Pagination(current_page=request.GET.get('page'),
                           all_count=numbers,
                           base_url=request.path_info,
                           query_params=query_params,
                           per_page=self.per_page)

        # =======================================================处理表格================================================
        all_data_obj = self.model_class.objects.all()[pager.start:pager.end]
        data_list = []

        # =====================================处理表格中的表头===============================
        verbose_name_list = []
        display_list = self.get_display_list()
        # 如果display_list里面有字段，表头我就让它显示我们定义的verbose_name，没有就让它显示表名
        if display_list:
            # 第一for用来设置表头的名字
            for key in display_list:
                if isinstance(key, FunctionType):
                    verbose_name = key(self, obj=None, is_header=True)
                    verbose_name_list.append(verbose_name)
                else:
                    verbose_name = self.model_class._meta.get_field(key).verbose_name
                    verbose_name_list.append(verbose_name)
        # 如果display_list没有字段，是个空的，表头就让它显示表名
        else:
            verbose_name_list.append(self.model_class._meta.model_name)

        # =========================================处理表格中的表体=====================================
        # 第二个for用来获取相关的数据
        for row in all_data_obj:
            row_list = []
            # 如果display_list里面有字段名，表内部就显示对应字段的数据
            if display_list:
                for key in display_list:
                    if isinstance(key, FunctionType):  # 判断是否是函数，是函数的话就就执行这个函数
                        row_list.append(key(self, obj=row, is_header=False))
                    else:
                        row_list.append(getattr(row, key))  # 不是函数就从数据库中获得对应的字段
            # 如果display_list里面没有字段， 我就让它显示表中的每一个对象，同时在对应表的类中重写__str__方法，显示一个默认值
            else:
                row_list.append(row)
            data_list.append(row_list)

            # =====================处理表格中是否有添加按钮=================
            add_btn = self.get_add_btn()
        return render(request, 'list.html',
                      {'data_list': data_list, 'verbose_name_list': verbose_name_list,
                       'pager': pager, 'add_btn': add_btn})

    def add_views(self, request):
        """
        对列表中的数据进行增加操作
        :param request:
        :return:
        """
        model_form_class = self.get_model_form()
        origin_url = self.reverse_list_url()
        if request.method == 'GET':
            form = model_form_class()
            return render(request, 'change.html', {'form': form})
        form = model_form_class(data=request.POST)
        if form.is_valid():
            self.save(form, is_update=False)
            return redirect(origin_url)
        return render(request, 'change.html', {'form': form})

    def change_views(self, request, pk):
        """
        对列表中的数据进行编辑或者删除操作
        :param request: 请求相关的所有信息
        :param pk: 传递过来的列表中某一个数据的唯一id， (\d+)
        :return:
        """
        origin_url = self.reverse_list_url()
        model_form_class = self.get_model_form()
        data_obj = self.model_class.objects.filter(id=pk).first()
        if not data_obj:
            return HttpResponse('要修改的对象不存在请仔细核对')
        if request.method == 'GET':
            form = model_form_class(instance=data_obj)
            return render(request, 'change.html', {'form': form})
        form = model_form_class(data=request.POST, instance=data_obj)
        if form.is_valid():
            self.save(form, is_update=False)
            return redirect(origin_url)
        return render(request, 'change.html', {'form': form})

    def del_views(self, request, pk):
        """
        对列表中的数据进行编辑或者删除操作
        :param request: 请求相关的所有信息
        :param pk: 传递过来的列表中某一个数据的唯一id， (\d+)
        :return:
        """
        origin_url = self.reverse_list_url()
        if request.method == 'GET':
            return render(request, 'delete.html', {'cancel': origin_url})
        self.model_class.objects.filter(id=pk).delete()
        return redirect(origin_url)

    # ====================================让每一个视图函数都有request请求的装饰器====================================
    # 为每一个视图函数写的装饰器，用来装饰视图函数，在下面的get_urls(self)方法中使用了
    def decorator_views(self, func):
        @functools.wraps(func)
        def inner(request, *args, **kwargs):
            self.request = request
            return func(request, *args, **kwargs)

        return inner

    # =============================获取路由(url和视图的对应关系，以及url的name三个属性)=======================================
    def get_urls(self):
        """
        里面获取url，如果想要减少url的数量可以通过，在self的相关类中，重写get_urls(self)方法即可
        :return:
        """
        patterns = [
            re_path(r'^list/$', self.decorator_views(self.list_views), name=self.get_list_name),
            re_path(r'^add/$', self.decorator_views(self.add_views), name=self.get_add_name),
            re_path(r'^edit/(\d+).html$', self.decorator_views(self.change_views), name=self.get_change_name),
            re_path(r'^del/(\d+).html$', self.decorator_views(self.del_views), name=self.get_del_name),
        ]
        patterns.extend(self.extra_urls())
        return patterns

    def extra_urls(self):
        """
        额外的增加url，默认是一个空的列表， 如果想要增加特定的url，只需要在self相关的类中重写extra_urls(self)方法即可
        :return:
        """
        return []


class StarkSite:
    """
    一个在路由分发之前导入的类，主要的工作是将我们定制好的路由放入到_registry列表中,并运用于在路由的配置
    """

    def __init__(self):
        self._registry = []
        self.app_name = 'stark'
        self.namespace = 'stark'

    def register(self, model_class, handler_class=None, prev=None):
        """
        在分发路由之前，我们去每一app的apps.py文件中进行相关的操作
        因为在路由分发之前会去每一个app的配置文件中进行操作，所以我们在apps.py文件中引用这个方法就能在路由分发之前，做一些操作
        完成自动生成相关的url
        我们的目的是在路由分发之前，定制好相关的路由(url和视图的对应关系) 把它放在一个_registry列表中，等到路由分发的时候，能够自动的从
        _registry中拿取我们定制好的路由
        :param model_class:是某个app中models.py文件中的某个类
        :param handler_class:处理视图函数所在的类
        :param prev:url的前缀
        :return:
        """
        if not handler_class:
            handler_class = StarkHandler
        self._registry.append(
            {'model_class': model_class, 'handler_class': handler_class(model_class, prev), 'prev': prev}
        )
        """
        我们想要拿到的_registry的形式：如下
        model_class是models.py模块中的对应列表的类
        handler_class 是我们自定义的一个类，它能够实现对对应的视图函数，传递进去model_class的目的是，在
                      编写对应的视图函数的时候，可以对指定的表进行操作
        [
            {'model_class': models.Department, 'handler_class': handler_class(model_class)},
            {'model_class': models.UserInfo},
            {'model_class': models.Host},
            
        ]
        """

    def get_urls(self):
        """
        拿取前面我们在每一个app中定制的路由(url和视图的对应关系)
        我们设置的每一个url为app_name/table_name/prev/param
            其中app_name 为app名， table_name 为表名  prev 为想要自定制添加的前缀  Parma 为list, add, change, del
        我们设置的每一个视图函数放在了StarkHandler里面，可以查找到对应的方法名
        我们设置的每一个url对应的name为 (app_name)_(table_name)_prev_param
            其中app_name 为app名， table_name 为表名  prev 为想要自定制添加的前缀  Parma 为list, add, change, del
        :return:
        """
        patterns = []
        for item in self._registry:
            model_class = item['model_class']
            handler = item['handler_class']
            app_name = model_class._meta.app_label  # 通过当前类获取所在app的名称
            table_name = model_class._meta.model_name  # 通过当前类来获取由类创建的表名称
            prev = item['prev']
            if prev:
                patterns.append(re_path(r'%s/%s/%s/' % (app_name, table_name, prev), (handler.get_urls(), None, None)))
            else:
                patterns.append(re_path(r'%s/%s/' % (app_name, table_name), (handler.get_urls(), None, None)))

        return patterns

    @property
    def urls(self):
        """
        在跟路由的urls.py文件中传入，site.urls 里面包含了我们定制好的
        :return: 返回我们定制好的urls, name, namespace
        """
        return self.get_urls(), self.app_name, self.namespace


site = StarkSite()
