#! /usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask,jsonify, request
from flask_pymongo import PyMongo
import pymongo


from utils import load_pickle,dump_pickle
import json
from datetime import datetime

from create_img import create_result
from extract_srt import get_file_info, extract_frames
from config import MONGODB_IP


app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'movie_srt'
# app.config['MONGO_URI'] = 'mongodb://root:root@172.28.0.2:27017/movie_srt'  

# mongo = PyMongo(app)


@app.route("/")
def index_():
    return "hello flask"


@app.route("/movies",methods=['GET'])    
def get_movies():
    client = pymongo.MongoClient(f"mongodb://root:root@{MONGODB_IP}:27017/")

    collection_movie = client["sub_movies"]['movies']
    movie_name = {}
    for item in collection_movie.find(projection={'_id': False}):
        score = [s['score'] for s in item['score_ls'] if s['type']=='豆瓣' ]
        item['score'] = score[0] if score!=[] else '0'
        movie_id = item['movie_id']
        # 是否完成
        item['ifFinish'] = False

        movie_name[movie_id] = item

    # 降序排列
    out = list(movie_name.values())
    move_name_items = sorted(out,key=lambda x:x['score'],reverse=True)   # 去除ID

    # move_name = [{} for d in move_name]
    print("move_name:", move_name_items)

    resData = {
        "resCode":0,
        "data":move_name_items,
        "message": "本次文本说明",
    }
    return jsonify(resData)


@app.route("/change_movie",methods=['POST'])
def change_movie_info():

    # 抽取数据
    get_data = json.loads(request.get_data(as_text=True))
    movie_id = get_data['data']['item']['movie_info']['id']
    movie_status = get_data['data']['item']['ifFinish']

    # print(movie_id,movie_status)

    client = pymongo.MongoClient(f"mongodb://root:root@{MONGODB_IP}:27017/")
    collection_movie = client["movie"]['movie']
    collection_movie_detail1 = client["sub_movies"]['movie_detail']
    collection_movie_detail2 =  client["sub_movies"]['movies']

    # 更新数据
    print(list(collection_movie.find({"id":movie_id})))
    result_update = collection_movie.update(   {'id':{'$eq':movie_id}},
                                        {'$set':{'ifFinish':movie_status}},
                                        upsert=True,
                                        multi=True
                                        )

    # 获取id 的明细数据
    try:
        result_detail1 = list(collection_movie_detail1.find({'movie_id':movie_id},projection={'_id': False}))[0]
    except:
        result_detail1 = {"result_detail1":"获取result_detail1数据失败"}
    try:
        result_detail2 = list(collection_movie_detail2.find({'movie_id':movie_id},projection={'_id': False}))[0]
    except:
        result_detail2 = {"result_detail2":"获取result_detail2数据失败"}

    result = {**result_update,**result_detail1,**result_detail2}


    # print(list(collection_movie.find({"id":movie_id})))
    data = "数据修改成功"
    resData = {
            "resCode":0,
            "data": result,
            "message": "本次文本说明",
        }
    return jsonify(resData)


@app.route("/movie_srt/<movie_id>",methods=['POST'])
def get_srt(movie_id):
    # 连接数据库
    client = pymongo.MongoClient(f"mongodb://root:root@{MONGODB_IP}:27017/")

    collection_movie = client["movie"]['movie']
    move_name = collection_movie.find({'id':movie_id})[0]['movie']
    print("move_name:", move_name)

    # movie_name = '最初的梦想'
    # subs_list = load_pickle(f"../data/{movie_name}/srt/sub_list.pkl")

    # 创建数据库
    db_srt = client["movie_srt"]

    collection = db_srt[movie_id]
    subs_list = list(collection.find(projection={'_id': False}))
    print(subs_list[0])
    data = {"name":move_name, "data":subs_list}

    resData = {
        "resCode":0,
        "data":data,
        "message": "本次文本说明",
    }
    return jsonify(resData)


# 抽取电影 截图 
@app.route("/movie_srt/<movie_id>/frame",methods=['POST'])
def send_frames_back(movie_id):
    if request.method =='POST':
        get_data = json.loads(request.get_data(as_text=True))
        print(get_data)
        
        key = get_data['key']
        secretKey = get_data['secretKey']
        timeshift = float(get_data['params']['timeshift'])
        # key = "最初的梦想"

        # data = get_data
        # use_content = get_data['params']['ifContent']
        # fontsize = int(get_data['params']['fontSize'])


        # 获取路径
        video_file, _, imgs_path = get_file_info(key)

        # 根据传入数据 输入开始和结束时间, 生成电影截图  # 同时考虑时间的偏移
        start = float(get_data['data']['start'])  + timeshift
        end = float(get_data['data']['end']) + timeshift
        print("时间：",start, end)
        img_save = extract_frames(video_file,imgs_path,start,end)

        resData = {
            'resCode': 0,
            'data':[img_save],
            'message':"返回结果"
        }
        return jsonify(resData)
    else:
        resData = {
            'resCode':1,
            'data':[],
            'message':'请求方法错误'
        }
        return jsonify(resData)



# 生成 图片
@app.route("/movie_srt/<movie_id>/create",methods=['POST'])
def create_srt_img(movie_id):
    if request.method =='POST':
        get_data = json.loads(request.get_data(as_text=True))
        print(get_data)
        
        key = get_data['key']

        secretKey = get_data['secretKey']
        use_content = get_data['params']['ifContent']
        fontsize = int(get_data['params']['fontSize'])

        # 根据传入数据 生成图片
        result_img = create_result(get_data,use_content=use_content,fontsize=fontsize)

        dt =  datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        img_save = f"../data/{key}/result/result_{dt}.png"
        result_img.save(img_save)

        print(img_save)
        print("save data ...")
        # 插入数据库
        client = pymongo.MongoClient(f"mongodb://root:root@{MONGODB_IP}:27017/")

        collection_srt_select = client["movie"]['movie_srt_select']

        get_data['img_result'] =  img_save
        result = collection_srt_select[movie_id].insert_one(get_data)

        # dump_pickle(get_data,"./get_data.pkl")


        resData = {
            'resCode': 0,
            'data':[img_save],
            'message':"返回结果"
        }
        return jsonify(resData)
    else:
        resData = {
            'resCode':1,
            'data':[],
            'message':'请求方法错误'
        }
        return jsonify(resData)





if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)