##### 1.git相关的命令

###### 1.git一般命令

```
git --version 查看git相关的版本
git init 初始化git
git status 检测当前文件所处的状态
git add file_name/. 管理指定的文件
git commit -m '版本描述信息'  向本地提交版本信息
git log  查看历史版本
git reflog 查看回滚之后的版本
git log --grpah --prettry=format "%h %s" 以更加美观的形式查看版本
```

###### 2.git版本相关的命令

```
git reset --hard 版本号 回滚到指定的版本
git reset --hard 标签号 快速回滚到指定版本
git reset --soft 版本号 从版本库回滚到指定版本的暂存区
git reset --mix 版本号 从版本库回滚到指定版本的文件变动区
git reset HEAD 从当前版本的暂存区回滚到文件变动区
git checkout + git restore 文件名 从当前版本的变动区回滚到已控制文件区域
```

###### 3.git分支相关的命令

```
git branch 查看当前分支
git branch dev 创建一个dev分支
git checkout dev 跳转到dev分支
git checkout -b dev 在没有dev分支的情况下创建一个dev分支并跳转
git branch -D dev 强制删除一个分支
git merge 分支名 合并指定的分支（直接使用merge合并会产生分叉）
```

###### 4.git与远程仓库相关联的命令

```
git remote add origin url地址 连接到指定的url地址并取一个origin的别名
git push -u origin 分支名 将指定的分支上传到远程仓库
git push origin master -f 将当前master分支的版本强制上传到远程的厂库
git pull origin 分支名 从远程仓库拉取指定的分支
git clone 地址 克隆url地址里面的所有内容，这里还建立了连接，默认别名为origin
git fetch origin dev + git merge origin dev/git rebase origin dev 等同于git pull origin dev 
git push origin --tag 将tag标签传递到远程仓库
```

###### 5.git中rebase相关的命令

+ rebase有三大作用

  + 合并记录

    ```
    git rebase -i HEAD~3 合并最近的三次记录
    ```

  + 不产生分叉的情况下合并分支

    ```
    git rebase master + git checkout master + git merge dev
    ```

  + 从远程仓库用变基的形式拿取指定的分支

    ```
    git pull --rebase origin 分支名
    ```

###### 6.git中配置的相关命令

1. 在本地文件配置(配置文件写入到.git/config)

   ```
   git config --local user.name 'fengxiaozi-liu'
   git config --local user.email '1969397913lh@'
   git remote add origin url地址 默认放在了本地的配置文件中
   ```

2. 设置全区配置(配置文件在~/.gitconfig中)

   ```
   git config --global user.name 'fengxiaozi-liu'
   git config --global http.proxy 代理地址
   git config --global http.sslVerify false 取消认证
   ```

3. 设置系统配置

   ```
   git config --system user.name 'fengxiaozi-liu'
   ```

4. 使用beyondcompare来快速解决冲突的配置

   1. 先进行相关的配置

      ```
      git config --local merge.tool bc3
      git config --local mergetool.path 'C:/Program Files/Beyond Compare 4'
      git config --local merge.tool keepbackup false
      ```

   2. 遇到冲突够调用

      ```
      git mergetool
      ```

##### 2.git的三大工作区

+ 工作区：在这里文成代码的编写，文件状态是红色
+ 暂存区：文件书写后用git管理起来的区域，文件状态是绿色
+ 版本库：上传到指定版本之后的区域，文件状态是白色

##### 3.git中的.gitingore文件

+ 作用：

  可以帮助git忽略掉那些没有管理的文件

+ 步骤

  1. 创建一个.gitingore文件
  2. 将不想管理的文件放到.gitingore文件中

+ 在.gitingore中文件的书写形式

  ```
  a1.txt 直接书写指定的文件
  ！a.txt 用！取反，意思就是管理起来
  *.txt  用正则表达式来判断
  file/  书写文件夹形式， 凡是在这个文件下的都不做管理
  ```

+ 参考文档

  具体的可以参考github中的gitingore模块

##### 4.git中免密登录

+ 介绍

  + 使用三种方式来完成免密登录

+ 第一种方式：在url中体现

  ```
  原来的地址：https://github.com/dbhot-liu/dbhot.git
  修改后的地址：https://用户名：密码@github.com/dbhot-liu/dbhot.git
  使用这种形式之后不需要重复的输入密码，这是以往的版本
  ```

+ 第二种方式在：ssh实现

  1. 使用ssh-keygen来生成秘钥(生成的公钥和私钥默认放在~/.sh下，公钥为id_rsa.pub, 私钥为id_rsa)

  2. 拷贝公钥的内容到github中

  3. 在git中配置ssh连接

     ```
     git remote add origin ssh地址
     ```

  4. 在以后的使用过程中就能够免密登录了

+ 第三种方式(git会自动的创建一个管理凭证)

  通过git创建的管理凭证直接进行登录即可

##### 5.git中的项目管理

1. issues
   + 主要是用来讨论话题和bug管理的
2. wiki
   + wiki是用来对相关的项目进行解释说明的，包括使用方式等等



