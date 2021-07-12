# -*- coding:utf-8 -*- 

import os
import pickle
import argparse
from PIL import Image
from datetime import datetime


import srt,json
# from tqdm import tqdm

from moviepy.editor import *
from moviepy.video.tools.subtitles import TextClip,SubtitlesClip

from utils import dump_pickle,load_pickle,check_path
from ass2srt.ass2srt import convert_ass_to_srt

 

def extract_frames(video_file,imgs_path,start,end):

    movie = VideoFileClip(video_file)
    # start = start.total_seconds()
    # end = end.total_seconds()
    time_gap = end - start
    time_mid =  (end - start)/2
    base_path = imgs_path + f'{start}_{end}'
    
    result_ls = []
    
    for i,t in enumerate([start,end,time_mid]):
        if i <= int(time_gap/2):
            movie.save_frame(base_path + f'_{i}.png',t = t)
            result_ls.append(base_path + f'_{i}.png')
    return result_ls

def process_subs(s):
    subs_dict = {}
    start = s.start.total_seconds()
    end = s.end.total_seconds()
    
    subs_dict["id"] = s.index
    subs_dict["start"] = start
    subs_dict["end"] = end
    subs_dict["content"] = s.content
    subs_dict["select1"] = False
    subs_dict["select1"] = False
    subs_dict["modify"] = s.content
    subs_dict['img_select'] = 0
    subs_dict["img_start"] = f"{start}_{end}"
    return subs_dict,start,end

def mian_process(movie_name):

    # 读取视频文件
    # movie = VideoFileClip(video_file)


    # 检查路径 
    check_path(movie_name)
    
    # 获取路径
    video_file, srt_file, imgs_path = get_file_info(movie_name)
   
    # 读取字幕文件
    with open(srt_file, 'r') as f:
        subs = srt.parse("".join(f.readlines()))
    
    subs_list = []
    
    for s in tqdm(subs):
        subs_dict,start,end = process_subs(s)
        # 抽取每段字幕文件
        subs_dict['img_ls'] = extract_frames(video_file, imgs_path, start, end)
        subs_list.append(subs_dict)
    
    return subs_list


def get_file_info(movie_name):
    # 基础路径
    base_path = f'../data/{movie_name}'
    # 电影字幕路径
    video_file_name = [f for f in os.listdir(base_path+"/movie")][0]
    video_file = base_path + f'/movie/{video_file_name}'
    
    # 字幕路径处理
    srt_file_name = [f for f in os.listdir(base_path+"/srt") if f.split('.')[-1] in ["sub","srt","ssa","ass","txt"]][0]
    srt_file = base_path + f'/srt/{srt_file_name}'

    if srt_file.endswith(".ass"):
        convert_ass_to_srt(srt_file)
        srt_file = srt_file[:-4] + ".srt"
    # 截图路径
    imgs_path = base_path + '/imgs/'

    return video_file, srt_file, imgs_path


def get_parser():
    # 生成argparse对象
    parser = argparse.ArgumentParser(description="帮助信息")
    
    # 添加需要的参数
    parser.add_argument('--movie_name', type=str, default="观视频")
    # 返回parser对象
    return parser  


if __name__ == "__main__":

    parser = get_parser()
    args = parser.parse_args() 
    # 读取字幕文件
    movie_name = args.movie_name

    # 处理电影数据
    subs_list = mian_process(movie_name)

    # 保存数据
    dump_pickle(subs_list,f"../data/{movie_name}/srt/sub_list.pkl")