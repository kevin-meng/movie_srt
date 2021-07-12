#!/bin/bash

# 在运行前要注意 修改monogodb 的数据库
# 安装 相关库
pip install flask_pymongo getsub caiyun srt pandas pymongo
# Flask 后台运行
nohup python /src/notebooks/backends/main.py > /src/notebooks/log/backend.txt 2>&1 &

# 运行 前段
cd /src/notebooks/frontends/moive_srt
nohup npm run serve > /src/notebooks/log/vue.txt 2>&1 &


#　运行本地图片镜像
cd /src/notebooks/server/
nohup nodemon router.js > /src/notebooks/log/img_server.txt 2>&1 &
