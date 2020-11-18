from django import template

# 变量名必须叫register，不能够更改
register = template.Library()


# 自定义一个模板语言的函数就自定义完成了
@register.filter
def my_upper(value):
    return value.upper()
