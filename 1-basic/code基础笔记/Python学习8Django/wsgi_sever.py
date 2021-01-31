from wsgiref.simple_server import make_server


# 1.建立一个路由的分发器，负责把URL匹配到对应的函数
# 2.开发好对应的业务函数
# 3.一个请求来了之后，先走路由分发器，如果找到对应的函数就执行，如果没有找到就返回404


def book():
    return 'book-package'


def cloth():
    return 'cloth-package'


def test():
    with open('./test.jpg', 'rb') as file:
        file = file.read()
        return file


# 设置一个路由返回分发器
def url_dispacher():
    url = {
        '/book': book,
        '/cloth': cloth,
        '/test': test
    }
    return url


def run_server(environ, start_response):
    url_list = url_dispacher()
    status = '200 ok'
    response_body = '今天你真好看'
    path = environ['PATH_INFO']
    if path == '/book':
        response_body = url_list.get(path)()
    elif path == '/cloth':
        response_body = url_list.get(path)()
    elif path == '/test':
        response_body = url_list.get(path)()
    else:
        status = '404 not found'
        response_body = '<p style="color:red"> 404 not found </p>'
    if isinstance(response_body, str):
        start_response(status, [('Content-Type', 'text/html;charset=utf8')])
        return [bytes(response_body, encoding='utf8')]
    else:
        start_response(status, [('Content-Type', 'jpg;charset=utf8')])
        return [response_body, ]


if __name__ == '__main__':
    httpd = make_server('localhost', 8000, run_server)
    httpd.serve_forever()
