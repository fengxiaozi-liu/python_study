"""
学习1不同电脑之间实现网络通信
    概念：
        简单来说，网络是用物理链路将各个孤立的工作站和主机连接到一起，组成数据链路，从而达到资源共享和通信的目的。
        使用网络的目的，就是为了联通多方然后进行通信，即把数据从一方传递给另外一方
        前面的学习编程写的程序都是单机的，既不能和其他电脑上的程序进行通信，为了让不同的电脑上运行的软件，之间能够相互的传递数据，就需要借助网络功能的实现
        ISP: 网络服务运营商 局域网连接到宽带再连接到广域网
ip地址：ip地址要在同一个网段才能通信
    ip地址：192.168.31.100     是八个二进制表示的1111 1111 转换成十进制就是255
    子网掩码：255.255.255.0    按照按位与运算
    网段：192.168.31.x
        x表示的是主机位
        主机位全0表示网络位
        主机位全1表示广播位
        网段的判断要与子网掩码联系在一起判断
    点分十进制：
        ip地址的每一位都是用八个二进制表示的把每一位转换成十进制然后用点分开就是点分十进制
    分类：
        A类：

            地址：   01111111 11111111 11111111 11111111  使用七位表示网络最高位是0
            子网掩码：11111111 00000000 00000000 00000000
            A类地址的网络 1.0.0.0 ==> 126.255.255.254 127开头的和0.0.0.0是特殊的ip地址
        B类
            以10开始
            2个字节的网络+网络位14位+主机位有16位
        C类
            以110开始
            3字节的网络和1字节的主机组成
        D类
            以1110开始
        E类
            以11110开始
    注意：
        每一个字节都为0的地址表示当前主机
        ip地址中的每一个字节都为1的表示当前子网的广播地址
        ip地址中以1111开头的E类地址保留用于实验
        ip地址不能以十进制127开头，以127开头的ip地址用于回路的测试
        网络的ID的第一个八位组也不能全置为0，全0表示网络
    DHCP服务器
        作用：
            用来自动的分配ip地址
        举例：
            如果连接上了路由器，那么路由器就是一个DHCP服务器
    DNS
        作用：
            把域名解析成ip地址

网络通信方式
    直接通信
    集线器通信
    使用switch交换机
    使用路由器连接多个网络


    MAC地址：在设备与设备之间数据通信时用来标记收发双方（网卡的序列号）
    IP地址：在逻辑上标记一台电脑，用来指引数据包的收发方向（相当于电脑的序列号）
    网络掩码：用来区分ip地址的网络号和主机号
    默认网关：当需要发送的数据包的目的ip不在本网段时，就会发送给默认的一台电脑成为网关
    路由器：连接多个不同的网段，让他们之间可以进行收发数据，每次收到数据后，ip地址不变，但是mac地址会变化
    http服务器：提供浏览器能够访问的数据

端口
    作用：
        不同电脑之间区分不同的程序
    端口号：
        1.0-65536
        2.0-1024不要用,系统上一些重要的服务在使用
        3.找一个空闲的端口号

pid
    作用
        不同的电脑之间使用pid区分不同的程序

socket
    不同的电脑之间实现通信
        ip地址可以标识网络中的主机，而传输层的协议+端口可以卫衣标识主机的用用程序（进程）。这样利用ip地址、协议、和端口就可以标识网络的进程
        网络中的进程通信可以利用这个标志与其他进程进行交互
    什么是socket：
        进程间通信的一种方式，可以让不同的进程之间实现通信
    创建：
        import socket
        socket.socket(Address Family,Type)
        函数socket.socket可以创建一个socket 该函数有两个参数
        Address Family 可以选择AF_INET（用于internet进程通信）或者AF_UNIX(用于同一台机器进程间的通信)
        Type 套接字类型，可以是SOCK_STREAM（流程套接字，主要用于TCP协议）或者SOCK_DGRAM（数据报套接字，用于UDP）协议

udp
    没有严格的客户端和服务器的区别
    在发送之间需要绑定端口号才能找到它
        s.bind(('ip地址',端口号))
        s.sendto(数据,('ip地址',端口号))
        接收数据用recvfrom(num)
tcp
    客户端
        在客户端和服务器面向连接的协议
        在发送数据之前必须要和服务器之间建立连接 否则数据不能发送出去
            对象名.connect(('ip地址',端口号))
            对象名.send(data)
    服务端
        接收数据需要两个函数 accept recv
        accept 接收到的是一个元组 第0个是客户端传递的socket连接 第1个是包含客户端的ip地址和端口号的元组
        recv(1024)是拿到客户的发送的具体消息是以二进制的方式接收的，因此拿到后需要解码

"""
























































