# 剧中台词对话长图拼接和分享网站项目【剧中人说】

### 一、项目背景
**是否有一部电影中的对白，戳中你，引发你的共鸣？**  **我有！！！** 

##### 开发项目的动因：
  1. 有想将影视剧中对面台词保存和分享的冲动。
  2. 手动截图拼接过于枯燥和低效。
  3. 目前我没有发现满足我需求的工具。

##### 项目的目标：
- 基于影视剧中的对话，生成长图便于分享和保存的网站。

### 二、软件架构
架构说明
项目采用前后端分离进行开发。 前端采用 Vue3 + Bootstrap ，后端采用 Flask ，数据库基于 MongoDB 。
影视数据基于 Python 爬虫下载，电影介绍从豆瓣抓取。

![](https://gitee.com/kevin777/wechat_pictures/raw/master/2021-7-10/1625924967020-image.png)

网站截图：

![](https://gitee.com/kevin777/wechat_pictures/raw/master/2021-7-11/1625976219371-image.png)


![](https://gitee.com/kevin777/wechat_pictures/raw/master/2021-7-11/1625976502469-image.png)




### 三、安装教程

1. 项目提供基于docker的安装环境。可通过`docker-compose up `一键启动。
2. 此外，项目本地部署时，为了解决vue3图片动态绑定的问题，利用 nodemon 进行本地静态资源托管解决。
3. 项目初始化若不成功，用`./init.sh` 可手动启动。



### 四、使用说明
1. 项目通过影视剧中的字幕文件，勾线对应台词向后端发送请求，对影视剧进行截图处理，返回最多3张备选截图，供用户可挑选。
2. 用户勾选多句想要生成长图的对白，可向服务器发送对应请求。
3. 服务器反回对应长图，供用户预览下载。

![](https://gitee.com/kevin777/wechat_pictures/raw/master/2021-7-12/1626102975316-image.png)


**注：** 长图通过两种模式供选择：
  - 原片字幕
  - 文本字幕
  
  具体区别如下：

![](https://gitee.com/kevin777/wechat_pictures/raw/master/2021-7-12/1626103321707-image.png)

### 五、项目结构
项目结构
```
└── movie_srt
    ├── backends            # ####  后端部分  ####  
    │   ├── fonts             # 字幕字体文件
    │   │   ├── msyhbd.ttc
    │   │   └── msyh.ttc
    │   ├── ass2srt           # 字幕转换文件
    │   ├── config.py
    │   ├── create_img.py     # 字幕截图抽取程序
    │   ├── extract_srt.py    # 截图生成程序
    │   ├── main.py           # 后端主程序
    │   └── utils.py
    ├── init.sh               # 服务启动脚本
    ├── log                   # 日志存放位置
    ├── docker-compose.yml    # ** 项目 docker 环境 启动文件
    ├── Dockerfile            # 主要镜像 dockerfile 
    ├── mongo-dockerfile      # 数据库镜像 dockerfile
    ├── frontends           # ###  前端部分  ####
    │   ├── moive_srt    
    │   │   ├── public
    │   │   ├── src
    │   │   │   ├── apis
    │   │   │   ├── App.vue
    │   │   │   ├── assets
    │   │   │   ├── components  
    │   │   │   ├── main.js
    │   │   │   ├── router
    │   │   │   ├── store
    │   │   │   ├── styles
    │   │   │   ├── types
    │   │   │   ├── utils
    │   │   │   └── views
    │   │   │       ├── CreateSrt.vue   
    │   │   │       ├── Home.vue        # 电影主页
    │   │   │       └── MovieSrt.vue    # 长图生成 字幕编辑 页面
    │   │   └── vue.config.js
    ├── README.md
    ├── db                 # ### 数据库部分 ###
    │   └── mongo            # 数据库文件
    ├── script               # 数据库初始化脚本
    │   ├── mongo
    │   ├── mysql
    │   ├── nginx
    │   └── redis
    ├── data
    │   ├── cover            # 封面图
    │   └── 最初的梦想　    　　#　电影名
    │       ├── imgs　      　# 截图文件
    │       ├── movie        # 电影文件
    │       └── srt          # 电影字幕文件
    └── server    # 本地静态文件托管程序
        └── router.js

```

### 六、参考项目
特别说明，该项目算是自己自学 Vue3 后，开发的第一个综合性的练手项目。其中，不免有写 bug。架构以及技术选型方面存在诸多不足。欢迎批评指正和交流。

![](https://gitee.com/kevin777/wechat_pictures/raw/master/2021-7-13/1626105981019-image.png)


另外，项目开发中，感谢以下开源项目：
- [books](https://github.com/alexhunter1943/books.git)
- [ass2srt-python](https://github.com/locobastos/ass2srt-python.git)


