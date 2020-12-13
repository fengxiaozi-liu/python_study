class PageInfo:
    """
    这是一个自定义的分页系统的类,里面含有有关分页的方法
    参数
        self.current.page: 当前页
        numbers：表示总数据个数
        per_page：表示每页显示多少条数据
        base_url:表示的是要跳转的url地址
        show_page_number：表示一个页面最多显示多少个标签（ 1 2 3 4 5）
    函数：
        def start：表示当前页应该从数据库中的第几个数据开始
        def end：表示当前页应该在第几个数据结束
        def pager：处理下面的数字标签，在一个页面中应该显示多少个数字标签，显示标签的样式，等等
    """
    def __init__(self, current_page, numbers, per_page, base_url, show_page_number=5):
        self.current_page = current_page
        try:
            self.current_page = int(self.current_page)
        except TypeError as e:
            self.current_page = 1
        self.per_page = per_page
        a, b = divmod(numbers, per_page)
        if b:
            a += 1
        self.page_numbers = a
        self.show_page_number = show_page_number
        self.base_url = base_url

    def start(self):
        """
        当前页应该从数据库的哪个数据开始
        """
        start_data = (self.current_page - 1) * self.per_page
        return start_data

    def end(self):
        """
        当前页应在数据库的哪个数据结束
        """
        end_data = self.current_page * self.per_page
        return end_data

    def pager(self):
        """
        对页面的数字标签进行处理
        """
        page_list = []
        half = ((self.show_page_number - 1) / 2)
        half = int(half)
        if self.page_numbers < self.show_page_number:
            begin_page = 1
            stop_page = self.page_numbers + 1
        # 如果总页数大于5
        else:
            # 如果当前页数<=3,就让它显示1-5页
            if self.current_page <= half:
                begin_page = 1
                stop_page = self.show_page_number + 1
            # 如果当前页>3，就让他显示前面两个和后面两个
            else:
                if (self.current_page + half) < self.page_numbers:
                    begin_page = self.current_page - half
                    stop_page = self.current_page + half + 1
                else:
                    begin_page = self.page_numbers - self.show_page_number + 1
                    stop_page = self.page_numbers + 1
        if self.current_page <= 1:
            prev_page = '<li><a href="">上一页</a></li>'
        else:
            prev_page = '<li><a href="%s?page=%s">上一页</a></li>' % (self.base_url, self.current_page - 1)

        page_list.append(prev_page)
        for i in range(begin_page, stop_page):
            if i == self.current_page:
                temp = '<li class="active"><a href="%s?page=%s">%s</a></li>' % (self.base_url, i, i)
            else:
                temp = '<li><a href="%s?page=%s">%s</a></li>' % (self.base_url, i, i)
            page_list.append(temp)
        if self.current_page >= self.page_numbers:
            next_page = '<li><a href="">下一页</a></li>'
        else:
            next_page = '<li><a href="%s?page=%s">下一页</a></li>' % (self.base_url, self.current_page + 1)
        page_list.append(next_page)
        return ''.join(page_list)