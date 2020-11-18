[TOC]

#### 根目录下的各大子目录

##### 常用的一些目录

| 目录  | 应放置文档内容                                               |
| :---: | :----------------------------------------------------------- |
| /usr  | 其实usr是Unix Software Resource的缩写， 也就是Unix操作系统软件资源所放置的目录，而不是用户的数据，应该将他们的数据合理的分别放置到这个目录下的次目录，而不要自行建立该软件自己独立的目录。<br />所有系统默认的软件(distribution发布者提供的软件)都会放置到/usr底下，因此这个目录有点类似Windows 系统的C:\Windows\ + C:\Program files\这两个目录的综合体，系统刚安装完毕时，这个目录会占用最多的硬盘容量 |
| /etc  | 系统主要的设定档几乎都放置在这个目录内，例如人员的帐号密码档、各种服务的启始档等等。 一般来说，这个目录下的各档案属性是可以让一般使用者查阅的，但是只有root有权力修改。<br /> FHS建议不要放置可执行档(binary)在这个目录中。 比较重要的档案有：/etc/inittab, /etc/init.d/, /etc/modprobe.conf,/etc/X11/,/etc/fstab,/etc/sysconfig/等等。 <br />另外，其下重要的目录有：/etc/init.d/ ：所有服务的预设启动script都是放在这里的，例如要启动或者关闭iptables的话： /etc/init.d/iptables start、/etc/init.d/ iptables stop。<br /> /etc/xinetd.d/ ：这就是所谓superdaemon管理的各项服务的设定档目录。<br />/etc/X11/ ：与X Window有关的各种设定档都在这里，尤其是xorg.conf或XF86Config这两个X Server的设定档。 |
| /bin  | 系统有很多放置执行档的目录，但/bin比较特殊。<br />因为/bin放置的是在单人维护模式下还能够被操作的指令。在/bin底下的指令可以被root与一般帐号所使用，主要有：cat,chmod(修改权限), chown, date, mv, mkdir, cp, bash等等常用的指令。 |
| /lib  | 系统的函式库非常的多，而/lib放置的则是在开机时会用到的函式库，以及在/bin或/sbin底下的指令会呼叫的函式库而已 。<br />什么是函式库呢？你可以将他想成是外挂，某些指令必须要有这些外挂才能够顺利完成程式的执行之意。<br />尤其重要的是/lib/modules/这个目录，因为该目录会放置核心相关的模组(驱动程式)。 |
| /sbin | Linux有非常多指令是用来设定系统环境的，这些指令只有root才能够利用来设定系统，其他使用者最多只能用来查询而已。<br />放在/sbin底下的为开机过程中所需要的，里面包括了开机、修复、还原系统所需要的指令。<br />至于某些伺服器软体程式，一般则放置到/usr/sbin/当中。<br />至于本机自行安装的软体所产生的系统执行档(system binary)，则放置到/usr/local/sbin/当中了。常见的指令包括：fdisk, fsck, ifconfig, init, mkfs等等 |
| /home | 这是系统预设的使用者家目录(home directory)。 在你新增一个一般使用者帐号时，预设的使用者家目录都会规范到这里来。比较重要的是，家目录有两种代号：<br />~ ：代表当前使用者的家目录，而 ~guest：则代表用户名为guest的家目录。 |
| /opt  | 这个是给第三方协力软体放置的目录 。 <br />什么是第三方协力软体啊？举例来说，KDE这个桌面管理系统是一个独立的计画，不过他可以安装到Linux系统中，因此KDE的软体就建议放置到此目录下了。 <br />另外，如果你想要自行安装额外的软体(非原本的distribution提供的)，那么也能够将你的软体安装到这里来。 不过，以前的Linux系统中，我们还是习惯放置在/usr/local目录下。 |

##### 关于根目录

1. 根目录简介

   除了这些目录的内容之外，另外要注意的是，因为根目录与开机有关，开机过程中仅有根目录会被挂载， 其他分区则是在开机完成之后才会持续的进行挂载的行为。就是因为如此，因此根目录下与开机过程有关的目录， 就不能够与根目录放到不同的分区去。

2. 不可与根目录分开的目录

   **/etc：**配置文件

   **/bin：**重要执行档

   **/dev：**所需要的设备文件

   **/lib：**执行档所需的函式库与核心所需的模块

   **/sbin：**重要的系统执行文件

关于/usr里面的内容

| 目录        | 应放置文件内容                                               |
| ----------- | ------------------------------------------------------------ |
| /usr/local/ | 统管理员在本机自行安装自己下载的软件(非distribution默认提供者)，建议安装到此目录， 这样会比较便于管理。<br />举例来说，你的distribution提供的软件较旧，你想安装较新的软件但又不想移除旧版， 此时你可以将新版软件安装于/usr/local/目录下，可与原先的旧版软件有分别啦。 你可以自行到/usr/local去看看，该目录下也是具有bin, etc, include, lib...的次目录 |
| /usr/bin/   | 绝大部分的用户可使用指令都放在这里。请注意到他与/bin的不同之处。(是否与开机过程有关) |
| /usr/lib    | 包含各应用软件的函式库、目标文件(object file)，以及不被一般使用者惯用的执行档或脚本(script)。 <br />某些软件会提供一些特殊的指令来进行服务器的设定，这些指令也不会经常被系统管理员操作， 那就会被摆放到这个目录下啦。要注意的是，如果你使用的是X86_64的Linux系统， 那可能会有/usr/lib64/目录产生 |
| /usr/sbin/  | 非系统正常运作所需要的系统指令。最常见的就是某些网络服务器软件的服务指令(daemon) |
| /usr/share/ | 放置共享文件的地方，在这个目录下放置的数据几乎是不分硬件架构均可读取的数据， 因为几乎都是文本文件。在此目录下常见的还有这些次目录：/usr/share/man：联机帮助文件<br />/usr/share/doc：软件杂项的文件说明<br />/usr/share/zoneinfo：与时区有关的时区文件 |

#### Linux中的环境变量配置攻略

##### Linux读取环境变量

读取环境变量的方法

+ ```shell
  # 命令显示当前系统定义的所有环境变量
  export 
  # 命令输出当前PATH环境变量值
  echo $PATH 
  ```

##### Linux中配置环境变量

以下面的例子进行解释说明

+ 系统 centos
+ 用户名liu
+ 需要配置环境变量的路径 /home/liu/mysql/bin

###### 方式1

`	export PATH`

使用`export`命令直接修改`PATH`的值,配置一个临时变量

```shell
export PATH=/home/liu/mysql/bin:$PATH
# 或者把PATH放在前面
export PATH=$PATH:/home/liu/mysql/bin
```

注意事项：

+ 生效时间：立即生效
+ 生效期限：当前终端有效，窗口关闭后无效
+ 生效范围：仅对当前用户有效
+ 配置的环境变量中不要忘了加上原来的配置，即`$PATH`部分，避免覆盖原来配置

###### 方式2

`vim ~/.bashrc`

通过修改用户目录下的`~/.bashrc`文件进行配置：

```shell 
vim ~/.bashrc
# 在最后一行加上
export PATH=$PATH:/home/liu/mysql/bin
# 激活环境
source ~/.bashrc
```

注意事项：

- 生效时间：使用相同的用户打开新的终端时生效，或者手动`source ~/.bashrc`生效
- 生效期限：永久有效
- 生效范围：仅对当前用户有效
- 如果有后续的环境变量加载文件覆盖了`PATH`定义，则可能不生效

###### 方式3

`vim ~/.bash_profile`

和修改`~/.bashrc`文件类似，也是要在文件最后加上新的路径即可：

```shell
vim ~/.bash_profile

# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
# 激活环境
source ~/.bash_profile
```

###### 方式4

`vim /etc/bashrc`

该方法是修改系统配置，需要管理员权限（如root）或者对该文件的写入权限：

```shell
# 如果/etc/bashrc文件不可编辑，需要修改为可编辑
chmod -v u+w /etc/bashrc

vim /etc/bashrc

# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
# 激活环境
source /etc/bashrc
```

注意事项：

- 生效时间：新开终端生效，或者手动`source /etc/bashrc`生效
- 生效期限：永久有效
- 生效范围：对所有用户有效

###### 方式5

`vim /etc/profile`

该方法修改系统配置，需要管理员权限或者对该文件的写入权限，和`vim /etc/bashrc`类似

```shell
# 如果/etc/profile文件不可编辑，需要修改为可编辑
chmod -v u+w /etc/profile

vim /etc/profile

# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
# 激活环境
source /etc/profile
```

注意事项：

- 生效时间：新开终端生效，或者手动`source /etc/profile`生效
- 生效期限：永久有效
- 生效范围：对所有用户有效

###### 方式6

`vim /etc/environment`

该方法是修改系统环境配置文件，需要管理员权限或者对该文件的写入权限：

```shell
# 如果/etc/bashrc文件不可编辑，需要修改为可编辑
chmod -v u+w /etc/environment

vim /etc/profile

# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
# 激活环境
source /etc/environment
```

注意事项：

- 生效时间：新开终端生效，或者手动`source /etc/environment`生效
- 生效期限：永久有效
- 生效范围：对所有用户有效

##### 环境变量的分类

+ 用户级别环境变量定义文件：`~/.bashrc`、`~/.profile`（部分系统为：`~/.bash_profile`）

+ 系统级别环境变量定义文件：`/etc/bashrc`、`/etc/profile`(部分系统为：`/etc/bash_profile`）、`/etc/environment`

  另外在用户环境变量中，系统会首先读取`~/.bash_profile`（或者`~/.profile`）文件，如果没有该文件则读取`~/.bash_login`，根据这些文件中内容再去读取`~/.bashrc`。

##### Linux中加载环境变量的顺序

1. /etc/environment
2. /etc/profile
3. /etc/bash.bashrc
4. /etc/profile.d/test.sh
5. ~/.profile
6. ~/.bashrc

#### 在Linux中下载一个安装包并把它运行起来的操作

###### 具体操作

```shell
# 从指定的位置下载一个压缩包
wget <url>
# 解压压缩包
tar -zxvf <file_name.tgz>
# 配置文件到指定的目录下
./configure –prefix=<文件路径>
# 进行编译和安装
make && make install
# 配置环境变量  这里配置的环境变量是对指定的用户进行的配置
vim ~/.bashrc 
export PATH=$PATH<文件绝对路径>
# 激活环境变量
source ~/.bashrc
```

###### 关于上面操作的基本信息

​	1. `./configure `是用来检测你的安装平台的目标特征的。比如它会检测你是不是有CC或GCC，并不是需要CC或GCC，它是一个		shell脚本。

2. make 是用来编译的，它从Makefile中读取指令，然后编译。

3. make install是用来安装的，它也从Makefile中读取指令，安装到指定的位置

###### 关于上面操作的详细解释

1. `./configure` 命令的作用

   这一步一般用来生成 Makefile，为下一步的编译做准备，你可以通过在 configure 后加上参数来对安装进行控制，比如代码:./configure –prefix=/usr 意思是将该软件安装在 /usr 下面，执行文件就会安装在 /usr/bin （而不是默认的 /usr/local/bin),资源文件就会安装在 /usr/share（而不是默认的/usr/local/share）。同时一些软件的配置文件你可以通过指定 –sys-config= 参数进行设定。有一些软件还可以加上 –with、–enable、–without、–disable 等等参数对编译加以控制，你可以通过允许 ./configure –help 察看详细的说明帮助。

2. make的作用

   这一步就是编译，大多数的源代码包都经过这一步进行编译（当然有些perl或python编写的软件需要调用perl或python来进行编译）。如果 在 make 过程中出现 error ，你就要记下错误代码（注意不仅仅是最后一行），然后你可以向开发者提交bugreport（一般在 INSTALL 里有提交地址），或者你的系统少了一些依赖库等，这些需要自己仔细研究错误代码。

   > 可能遇到的错误：make *** 没有指明目标并且找不到 makefile。 停止。问题很明了，没有Makefile，怎么办，原来是要	先./configure 一下，再make。

3. make insatll的作用

   这条命令来进行安装（当然有些软件需要先运行 make check 或 make test 来进行一些测试），这一步一般需要你有 root 权限（因为要向系统写入文件）

4. 扩展说明

   1. Linux的用户可能知道，在Linux下安装一个应用程序时，一般先运行脚本configure，然后用make来编译源程序，在运行make install，最后运行make clean删除一些临时文件。使用上述三个自动工具，就可以生成configure脚本。运行configure脚本，就可以生成Makefile文件，然后就可以运行make、make install和make clean。

   2. configure是一个shell脚本，它可以自动设定源程序以符合各种不同平台上Unix系统的特性，并且根据系统叁数及环境产生合适的Makefile文件或是C的头文件(header file)，让源程序可以很方便地在这些不同的平台上被编译连接。

   3. 这时，就可运行configure脚本了，运行configure脚本，就可产生出符合GNU规范的Makefile文件了： $ ./configure

      到此时，就可以运行make进行编译，在运行make install进行安装了，最后运行make clean删除临时文件。