#### LSI阵列卡BIOS选项

##### 主要几大板块

+ Configuration Management：查看逻辑盘信息、组件和删除逻辑盘、配置JBOD盘
+ Controller Management：设置控制卡(阵列卡)的参数，以及保存日志信息
+ Virtual Driver Management:查看逻辑盘信息和修改逻辑盘的高级选项
+ Driver Management:查看物理硬盘信息
+ Hardware Components:查看外接电容和背板信息

##### Configuration Management

###### create Virtual Drive

+ 主要是用来创建逻辑盘

+ | 参数                              | 作用                             | 具体细节                                                     |
  | --------------------------------- | -------------------------------- | ------------------------------------------------------------ |
  | select RAID Level                 | 选择指定的逻辑盘                 |                                                              |
  | select Driver From与Select Driver | 选择指定的驱动来管理逻辑盘       | select Driver From参数设置为Unconfigurd Capacity时，表示使用Unconfigured Good硬盘来组件逻辑盘。<br/>Select Driver From的参数是Free Capacity时，select Driver 选项变成Select Driver Group，当之前逻辑盘组件没使用最大容量时，其所在的Drive Group中剩余容量可通过此方式继续组建逻辑盘 |
  | virtual Drive Name                | 为逻辑盘创建一个名字             |                                                              |
  | virtual Drive Size                | 逻辑盘容量大小，默认是最大值     |                                                              |
  | Strip Size                        | 条带宽度，默认256kb              |                                                              |
  | read policy                       | 是否打开预读选项                 | read ahead 打开预读选项，No Read Ahead 关闭预读选项，Read Ahead在连续读取的时候，会提前捕捉下一个扇区数据读取到缓存模块，提升连续读取的速度 |
  | Write Policy                      | 开启或者关闭写缓存               |                                                              |
  | I/O Policy                        | I/O 策略                         | Cache I/O 先将数据读取到缓存中再从缓存中读到主机端<br/>Direct I/O 将数据同时读到缓存和主机端，当缓存中的数据再次读取时 直接从缓存中读取数据 |
  | Access Policy                     | 设置逻辑盘在OS 下的读写权限      | Read/Write Read only Blocked 三种模式                        |
  | Drive Cache                       | 设置物理缓存                     | Unchanged Eable Disable 三种模式                             |
  | Disable Background Initialization | 开启或者关闭后台进程初始化       | 新建RAID5成员数量不少于5个，RAID6成员盘不少于7个，5分钟后会自动的进行后台初始化 |
  | Default Initilization             | 组建完成后是否对逻辑盘进行初始化 | No不进行初始化，Fast初始化逻辑盘前100 M空间，Full初始化整个逻辑盘 |
  | Emulation Type                    | 仿真类型                         |                                                              |

###### create profile Based Virtual Driver

+ 创建逻辑盘，只能选择RAID级别和硬盘类型，其他参数创建过程无法修改

###### Make JBOD 

+ 创建一个JBOD盘，只有在raid模式下，JBOD打开才可以使用

###### Make Unconfigured Good

+ 将JBOD盘设置成Unconfigued Good硬盘。需要Unconfigured Good硬盘

###### Clear Configuration

+ 删除所有逻辑盘

###### Manage Foreign Configuration

+ 配置新插入硬盘的配置信息

###### 补充

+ RAID10内个Span需要两个硬盘，最少需要两个Span
+ RAID50每个Span需要三个硬盘，最少需要2个Span
+ RAID60每个Span需要四个硬盘，最少需要两个Span

##### Controller Management

###### basic Properties

+ 主要包括卡的型号，序列号，启动设备，pci槽位信息，fw版本，connectors数量，硬盘信息，逻辑盘数量

###### Advanced Controller Management

+ 包括保存控制卡日志信息，设置控制器接口的传输速率，管理逻辑盘的Consistency Check功能以及恢复出厂设置等功能

+ | 参数                                     | 功能                                        | 具体细节                                                     |
  | ---------------------------------------- | ------------------------------------------- | ------------------------------------------------------------ |
  | clear controller Events                  | 删除所有控制卡事件                          |                                                              |
  | save controller Events                   | 保存一份当前控制卡                          | 日志文件默认为TXT格式，可以保存到U盘等移动设备               |
  | save TTY Log                             | 保存控制卡固件终端日志                      | 用于出现问题时开发进行定位分析，知识部分诊断报告<br />若需要完整的诊断报告需要外接控制卡串口手机对应串口日志 |
  | Manage Link Speed                        | 设置控制卡各个Phy的接口速率                 | 可以将接口设置为3GB，6GB，12Gb                               |
  | Manage MegaRAID Advanced Software Option | 可以通过添加key的方式添加一些数据加密的功能 |                                                              |
  | Schedule Consistency Check               | 逻辑盘CC校检                                | 修复逻辑盘中的坏数据                                         |

###### Advanced Controller Properties

+ 包括查看控制器缓存信息，巡读设置，电源管理，热调功能设置，任务系统资源占用比率以及控制卡基本属性信息

+ | 参数                 | 作用                                                         | 具体细节                                                     |
  | -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | cache and Memory     | 显示控制卡的缓存容量以及CacheCade功能是否可用等信息          |                                                              |
  | Patrol Read          | 巡读模式                                                     | 巡读功能是一种预防措施，用于在驱动器故障能够<br />威胁数据完整性之前检测出硬盘驱动器错误。 |
  | Power Saving Setting | 电源管理                                                     | 设置spin down Unconfigured Good和Spin Down Host Spare盘(standby)<br />一段时间后是否进入Spin Down状态，通过降低机械硬盘盘片转速或直接关闭机械盘盘片马达从而达到省电目的<br />spinup Drive Count:设置每次上电硬盘数量<br/>spinup Delay:设置每次上电硬盘的间隔时间 |
  | Spare                | 热备盘相关设置                                               | Emergency Spare(紧急热备) 当组成逻辑盘的物理盘出现问题的时候，它就会将设置好的盘顶替那个坏掉的物理盘，来保证逻辑盘的稳定<br/>GlobalHotSpare:全局式式备份 Unconfiguration Good：占用式备份<br/><br/>Emergency for SMARTer:当逻辑盘中的成员盘出现预告警盘(Predicted Fail Cont为1)时触发紧急热备功能<br/><br/>Persistent Hot Spare: 功能开启时，在原热备盘槽位插入新硬盘，新硬盘会自动设置为热备盘<br/><br/>Replace Drive: 回拷功能，当新硬盘替换逻辑硬盘找那个的故障成员盘后，热备盘会将数据拷贝到新硬盘<br/><br/>Replace Drive on SMART Error:当检测到SMART Error时触发Replace功能 |
  | Task Rates           | 设置控制卡各个后台进程占用的系统资源频率，默认都是30，最大值为100 | 可设置选项卡包括<br />background Initilization Rate 后台初始化频率<br/><br/>Consistency Check Rate: cc校检频率<br/><br/>Patrol Read Rate:巡读频率<br/><br/>Rebuild Rate:重建频率<br/><br/>Reconstruction Rate: 重建频率 |

###### 阵列卡的中的其他属性

| 参数                              | 作用                                                         | 具体细节                                                     |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| alarm control                     | 蜂鸟计时器                                                   |                                                              |
| Auto Import Foreign Configuration | 自动导入外部设备                                             |                                                              |
| Boot Mode                         | 开机模式                                                     | Stop on Error显示启动过程遇到的错误并等待输入，在执行一些操作之前，固件不会继续进行引导过程<br/>Ingore Error:忽略错误，固件继续启动<br/>Pause on Error:由于硬件故障，固件可能会停止<br/>Safe mode on error:在启动的过程中，遇到错误引导控制器在安全模式下运行 |
| Controller BIOS                   | 阵列卡BIOS                                                   | 若系统引导盘在控制卡上面，则此选项需设置为Enabled系统才能够成功引导 |
| Maintain Drive Fail History       | 通过重新启动来跟踪不良硬盘功能                               |                                                              |
| SMART Polling                     | 设置控制卡获取硬盘SMART信息的轮询时间                        |                                                              |
| Stop Consistency Check on Error   | 当冗余逻辑盘进行cc校检的时候，如果遇到不良数据就会停止cc校检 |                                                              |
| JBOD Mode                         | 是否启动JBOD模式                                             |                                                              |
| Write Verify                      | 在刷新缓存之前验证数据时候已正确写入高速缓存中               |                                                              |

##### Virtual Driver Management

###### Operation

+ 选择操作选项

+ | 参数                      | 作用                   | 具体细节                                                     |
  | ------------------------- | ---------------------- | ------------------------------------------------------------ |
  | Start Locate              | 开启逻辑盘点灯定位     |                                                              |
  | Stop Locate               | 关闭逻辑点灯定位       |                                                              |
  | Delete Virtual Drive      | 删除虚拟逻辑盘         |                                                              |
  | Expand Virtual Drive      | 逻辑盘扩容             |                                                              |
  | Reconfigure Virtual Drive | 修改逻辑盘的级别       |                                                              |
  | Break Mirror              |                        | 举例<br />将raid 1拆分为两个raid 1 可以拿取一个到其他机台使用，此过程不可逆 |
  | Hide Drive Goup           | 隐藏硬盘组             | 使硬盘下所有的逻辑盘在os磁盘管理界面不可见                   |
  | Fast Initialization       | 快速初始化             | 只初始化逻辑盘前100M                                         |
  | Slow Initialization       | 慢速初始化             | 此过程的时间较长                                             |
  | Check Consistency         | 手动启动逻辑盘连续校检 | 检测并修复逻辑盘中坏损的数据                                 |
  | Virtual Drive Erase       | 逻辑盘擦除             | 擦除逻辑盘上所有的数据                                       |

###### Basic Properties

+ 基础属性

+ | 参数       | 作用            | 具体细节 |
  | ---------- | --------------- | -------- |
  | Name       | 逻辑盘名称<br/> |          |
  | Raid Level | 逻辑盘等级<br/> |          |
  | Status     | 逻辑盘状态      |          |
  | Size       | 逻辑盘大小      |          |

###### view Associated Drivers

+ 查看相关驱动程序

+ | 参数                      | 作用              | 细节 |
  | ------------------------- | ----------------- | ---- |
  | Status                    | online或者offline |      |
  | size                      | 大小              |      |
  | type                      | disk磁盘          |      |
  | Hardware Vendor           | 厂商信息          |      |
  | Associated Virtual Driver | 相关驱动          |      |

Advanced

+ 高级配置

+ 这个界面下包含两大模块，一是逻辑盘的属性，一个时逻辑盘设定

+ 逻辑盘属性

  + | 参数                | 作用             | 细节 |
    | ------------------- | ---------------- | ---- |
    | Mirror Data Size    | 镜像数据大小     |      |
    | Logical Sector Size | 逻辑磁盘扇区大小 |      |
    | Segment Size        | 分区大小         |      |

+ 逻辑盘设定

  + | 参数                              | 作用               | 细节                     |
    | --------------------------------- | ------------------ | ------------------------ |
    | Access                            | 支持可读可写功能   |                          |
    | Default Write Cache Policy        | 默认写返回设定     | 一般默认是写回           |
    | Disable Background Initialization | 是否关闭后台初始化 |                          |
    | Read Cache Policy                 | 读缓存的设定       | 一般都是读取相关头部信息 |
    | Drive Cache                       | 驱动缓存           |                          |
    | I/O                               | 输入或输出         |                          |
    | Emulation Type                    | 仿真接口类型       |                          |

##### Driver Management

###### Operation

+ | 参数                          | 作用                             |
  | ----------------------------- | -------------------------------- |
  | start Locate                  | 开始点灯定位                     |
  | Stop Locate                   | 结束点灯定位                     |
  | Initialization Drive:         | 初始化硬盘                       |
  | Drive Erase                   | 硬盘数据擦除                     |
  | Make Unconfigured Bad         | 将硬盘设置为Unconfigured Bad状态 |
  | Make JBOD                     | 制作JBOD盘                       |
  | Assign Global Hot Spare Drive | 分配全局热备盘                   |
  | Prepare For Removal           | 使硬盘处于安全可拔出状态         |

###### Advanced

+ 高级选型配置

+ | 参数                        | 作用                                                |
  | --------------------------- | --------------------------------------------------- |
  | Logical Sector Size         | 逻辑分区大小                                        |
  | Physical Sector Size        | 物理分区大小                                        |
  | Predicted Fail Count        | 顾名思义，当它的数量变成1的时候，会开启紧急热备功能 |
  | SAS Address                 | SAS物理地址                                         |
  | Drive Power State           | 硬盘电源状态                                        |
  | Cache Setting               | 缓存设置                                            |
  | Available Size              | 可用空间大小                                        |
  | Used Space                  | 已使用空间大小                                      |
  | Disk Protocol               | 磁盘协议                                            |
  | Device Speed                | 磁盘数据传输速度                                    |
  | Number of Connections       | 连接数量                                            |
  | Cryptographic Erase Capable | 密码擦除                                            |

##### Hardware Components

###### Battery Status

+ 电源状态

###### Temperature Status

+ 温度传感器

###### Fans

###### Power Supplies

###### Advanced

+ Battery Management
  + Type:电池型号
  + Status:电池状态
  + Capacitance:电池容量
  + Temperature:电池温度
  + Advanced:这里面列出了电池的详细信息

+ Enclosure Management
  + Vendor ID:厂商id
  + Enclosure ID: 背板ID
  + Enclosure Model:背板信息模式
  + Product Revision Level:
  + Number of Slots:插槽数量
  + Attached Drives:背板所连接的硬盘



