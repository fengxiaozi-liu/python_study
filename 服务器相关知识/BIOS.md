[TOC]

#### BIOS

##### 定义

+ BIOS是基本的输入和输出系统，它是在硬件系统上最基本的软件代码，是在操作系统OS之下的底层运行程序，它是处于计算机硬件和OS之间的抽象层

##### BIOS的各大主选项

| 选项名称     | 主要功能                                                     |
| ------------ | ------------------------------------------------------------ |
| Main菜单     | 主要是用来查看BIOS版本，内存容量，还可以对系统时间和日期进行设置 |
| Advanced     | 包含BIOS系统高级配置：PCI子系统 、USB、串口、网络配置        |
| IntelRCsetup | 包好CPU、内存、PCIe等设备信息，可以通过本级面实现主要设备的配置 |
| Server Mgmt  | 包含FRB、看门狗定时器、BMC网络配置、SEL 通过本界面实现对这些管理功能设置 |
| Security     | 安全设置 通过这个界面实现对用户密码的修改                    |
| Boot         | 实现启动功能控制，包括启动方式、启动顺序、启动过程等         |
| Save&Exit    | 这个界面是实现保存BIOS参数并且退出的                         |

##### BIOS各个主选项下的功能

###### Advanced(高级系统设置)

+ 串口

  | 名称                            | 作用                                       | 开启 | 关闭 |
  | ------------------------------- | ------------------------------------------ | ---- | ---- |
  | Serial Port Console Redirection | 将物理串口或者是虚拟串口映射到指定系统串口 |      |      |

+ PCI子系统

  + | 参数              | 作用                 | 开启                 | 关闭                                                         |
    | ----------------- | -------------------- | -------------------- | ------------------------------------------------------------ |
    | Above 4G Decoding | 4g以上的访问控制开关 | 开启4g以上的译码功能 | 关闭4g以上的译码功能                                         |
    | SR-IOV Support    | 虚拟化IO支持         | 系统虚拟化io功能开启 | 如果存在PCIE卡由os分配io资源，如果不支持PCIE卡则禁止io虚拟化功能 |

+ Network配置

  + | 参数               |
    | ------------------ |
    | ipv4 pxe support   |
    | ipv6 pxe support   |
    | pxe boot wait time |
    | media detect count |

+ USB 配置

  + | 参数                  | 作用                                                | 开启                     | 关闭                   |
    | --------------------- | --------------------------------------------------- | ------------------------ | ---------------------- |
    | Legacy usb support    | 用来开启或者关闭磁盘系统下USB设备功能               | 支持传统的USB设备        | 只支持efi文件的USB设备 |
    | XHCI hand-off         | 是否用USB XHCI协议                                  | 启动后可扩展主控制器接口 | 关闭后不可扩展         |
    | EHCI hand-off         | 是否在进入os模式之前将USB切花哪位USB2.0             |                          |                        |
    | port 60/64            | 端口仿真设置，启用此功能可以更好的支持USB键盘设备   |                          |                        |
    | USB transfer time-out | USB传输超时，一般设置超时时间是20s                  |                          |                        |
    | Device reset time-out | 设备复位超时，一般设置也是20s                       |                          |                        |
    | device power-up delay | 设备加电延时，就是设置USB主控制器报道的最大延时时间 |                          |                        |
    | mass storage devices  | 此项用于设置连接的USB设备的具体类型                 |                          |                        |

+ ISCSI 配置

  + 主要功能是在tcp/ip网络上的主机系统和存储设备之间进行大量 数据的封装可可靠性传输

###### IntelRCSetup(英特尔选项卡设置)

+ Processor Configuration(处理器配置)

  + | 参数                               | 作用                                                         | 开启                             | 关闭 |
    | ---------------------------------- | ------------------------------------------------------------ | -------------------------------- | ---- |
    | Intel VT for Devirected I/O (VT-d) | 虚拟化分配技术                                               | 加速数据传输和消除大部分性能开销 |      |
    | Hpyer-Threading                    | 超线程技术就是将一个物理单元变成两个逻辑单元，这样两个逻辑单元就可以同时执行多个任务 |                                  |      |

    补充：开启或者关闭虚拟化分配技术，默认是关闭。安装虚拟机时请开启。英特尔vt-d是英特尔虚拟化硬件架构的最新成员。VT-d能够改进应用的兼容性和可靠性，并且提供更高水平的可管理性，安全性，隔离性，和i/o性能，从而帮助VMM更好利用硬件

+ Advanced Power Management Configuration(对处理器供电进行高级配置)

  + | 参数                    | 作用                                      | 开启         | 关闭           |
    | ----------------------- | ----------------------------------------- | ------------ | -------------- |
    | Power Technology        | 电源省电模式设置                          | 使用省电设置 | 不支持省电模式 |
    | Config TDP              | 散热功能设计                              |              |                |
    | CPU P State Control     | 表明处理器处于省电模式仍旧能执行一些工作  |              |                |
    | CPU C State Control     | 表示处理器处于空闲状态(c0-c6 一共7个等级) |              |                |
    | CPU Advanced PM Turning | 电源管理的高级配置                        |              |                |

    补充：c0(激活): cpu在这一状态下接受指令处理数据

    ​		    c1(挂起): 可以节省CPU70%的能耗，所有处理器都必须支持这一功耗状态

    ​			c2(停止允许)： 处理器时钟频率和io缓冲被停止 

    ​			c3(深度睡眠); 总线频率和PLL均被锁定，在多核心系统下，缓存无效，在单核心系统下，内存被关闭，但缓存仍然有效

    ​			c4(更深度睡眠): 二级缓存的数据将有所减少

    ​			c5: 二级缓存被减为0

    ​			c6: 二级缓存减为0后，CPU核心电压变低

  + CPU  P  State control 界面配置

    + | 参数       | 作用                | 开启                                                         | 关闭                                 |
      | ---------- | ------------------- | ------------------------------------------------------------ | ------------------------------------ |
      | EIST       | 增强型SpeedStep技术 | 开启后会自动调整处理器电压和内核频率，从而减少平均功耗和平均热量并降低噪音 |                                      |
      | Turbo Mode | 超频模式开关        | 开启后，CPU利用率达到100%，运行频率根据CPU的核心数超过外频达到最大 | 在压力测试下，CPU运行频率为CPU的外频 |

  + CPU C State Control

    + | 参数                  | 作用                 | 开启                                                         | 关闭 |
      | --------------------- | -------------------- | ------------------------------------------------------------ | ---- |
      | package C State limit | 用来限制C状态        | 如果设置了c0/c1 状态，那么c2 状态就不起作用<br />如果限制了c2状态那么就不能进入更加节能的状态<br />默认是c6状态 |      |
      | CPU C3 Report         | 向os报告c3状态的开关 |                                                              |      |
      | CPU C6 Report         | 向os报告c6状态的开关 |                                                              |      |

  + CPU Advanced PM Turning

    + | 参数                    | 作用                                |
      | ----------------------- | ----------------------------------- |
      | Energy Performance BIAS | 能源性能管理模式                    |
      | Performance             | 最大限度保证CPU性能                 |
      | Balanced Performance    | 在保证了正常工作基础上保证CPU的性能 |
      | Balanced Power          | 保证正常工作基础上保证能源节省      |
      | Power                   | 最大限度节能                        |

+ Memory Configuration(内存配置)

  + | 参数             | 作用         |
    | ---------------- | ------------ |
    | total memory     | 查看总的内存 |
    | memory frequency | 查看内存频率 |

+ PCH Configuration(南桥配置)

  + | 参数                   | 作用     |
    | ---------------------- | -------- |
    | PCH SATA Configuration | 硬盘配置 |
    | USB Configuration      | USB配置  |

+ Server ME Configuration

###### Server Mgmt(服务配置)

+ | 参数                       | 作用                                                         | 开启               | 关闭               |
  | -------------------------- | ------------------------------------------------------------ | ------------------ | ------------------ |
  | Wait for BMC               | 系统开机时长设置                                             | 系统的开机时间较长 | 默认情况下是关闭的 |
  | FRB-2 Timer                | 可以理解为Post定时器开关<br />FRB-2 Time有两个选项<br />1.FRB-2 Time out(一般默认是6分钟)是在Post进行自我诊断的同时，如果有错误信息在post界面halt挂起若超过这个超时时间 ，它就会执行它的第二个选项<br />2.FRB-2 Timer policy (do nothing reset powr down power cycle) | 开启FRB-2定时器    | 关闭FRB-2定时器    |
  | os watchdog Timer          | 开启此此功能后，系统进入os系统<br />os watchdog timer 使用时。如果发生系统故障， os wtd timer time-out(默认是十分钟)，看门狗定时器执行相应的策略(do nothing reset power down power cycle) | 开启看门狗定时器   | 关闭看门狗定时器   |
  | System Event log           | 可以指定系统事件达清除日志的方式，当系统日志达到最大记录数量之后的处理方式，日志状态码 |                    |                    |
  | BMC  Network Configuration | 设置BMC网口类型。有管理网口(Dedicated)和业务网口(Shared)的划分 |                    |                    |
  | BMC User setting           | Channel NO 要设置为1或2<br />在BMC下不能连接KVM需要在点击BMC下configuration->User修改设置，勾上KVM |                    |                    |

###### Security(安全)

+ 太简单 过

###### Boot(开机设置)

+ Boot参数说明

+ | 参数                 | 作用                                                       |
  | -------------------- | ---------------------------------------------------------- |
  | Setup Prompt Timeout | 设置进入BIOS设置提示信息长短                               |
  | Bootup Numlock State | 开机后数字键盘指示灯状态设置                               |
  | Quiet Boot           | 选择Post自检信息和Logo启动屏幕显示                         |
  | Add New Boot Option  | 添加新的启动项，此功能在UEFI模式下可用，添加.efi可启动文件 |
  | Delete Boot Option   | 删除启动项                                                 |

Save&Exit

+ 界面参数说明

+ | 参数                     | 作用                     |
  | ------------------------ | ------------------------ |
  | save change and exit     | 保存修改并退出           |
  | discard change and exit  | 放弃修改并退出           |
  | save change and exit     | 保存修改并退出           |
  | discard change and reset | 放弃修改并重启           |
  | save change              | 保存修改                 |
  | discard change           | 放弃修改                 |
  | restore defaults         | 恢复出厂设置             |
  | save ad user defaults    | 保存成用户默认设置       |
  | restore user defaults    | 恢复用户默认设置         |
  | boot override            | 选择从以下启动设备中启动 |

  