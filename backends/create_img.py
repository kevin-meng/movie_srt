# -*- coding:utf-8 -*- 

import os
from PIL import Image
from datetime import datetime
import pickle

from moviepy.editor import *

import srt,json
from tqdm import tqdm
from moviepy.video.tools.subtitles import TextClip,SubtitlesClip
from PIL import ImageFont,ImageDraw,Image

from extract_srt import extract_frames,get_file_info


def data_process(d,video_file,imgs_path,types='cover',use_content=False):
    out= dict()
    out['type'] = types
    out['content'] =d['modify']
    start = d['start']
    if d['img_ls'] != []:
        out['img'] = d['img_ls'][d['img_select']]
    else:
        if (use_content) & (types == 'srt'):
            img_file = '../data/cover/cover.png'
        else:
            # 自动抽取图片
            img_file = imgs_path + f'{start}_{start}_0.png'
            # 抽取图片
            movie = VideoFileClip(video_file)
            movie.save_frame(img_file,t = start)
        # 添加截图
        out['img'] = img_file
    return out


def extract_data(get_data):
    movie_name = get_data['key']
    use_content = get_data['params']['ifContent']

    # print(movie_name)
    get_data_list = sorted(get_data['data'],key=lambda x: x['id'])
    
    # 获取路径
    video_file, srt_file, imgs_path = get_file_info(movie_name)

    result_list = []
    for d in get_data_list:
        if d['select1']==True:
            out = data_process(d,video_file,imgs_path,types='cover')
            result_list.append(out)


        if d['select2']==True:
            out = data_process(d,video_file,imgs_path,types='srt',use_content=use_content)
            result_list.append(out)

    return result_list


def get_img_size(result_list,box_img_ratio = (0.0, 0.0, 1.0, 0.85),box_srt_ratio=(0.0, 0.85, 1.0, 0.95)):
    
    img = Image.open(result_list[0]['img'])
    width,height = img.size

    n_cover = len([c for c in result_list if c['type']=='cover'])
    n_srt = len([c for c in result_list if c['type']=='srt'])    
    
    # 封面区域的尺寸
    left_i,upper_i,right_i,lower_i= box_img_ratio

    # 字幕区域的尺寸
    left_s,upper_s,right_s,lower_s= box_srt_ratio

    box_dict = {}
    box_dict['cover'] = (int(width*left_i),int(height*upper_i),int(width*right_i),int(height*lower_i))
    box_dict['srt'] =  (int(width*left_s),int(height*upper_s),int(width*right_s),int(height*lower_s))
    
    
    # 背景图 尺寸
    # width_new = int((right_i - left_i) * width)
    # height_new = int(n_cover * (lower_i - upper_i) * height + n_srt * (lower_s - upper_s) * height)
    # box_bg_img = (width_new,height_new)
    return box_dict

def img_crop(img_name,types,box,content,use_content=False,fontsize=50):
    img = Image.open(img_name)
    img_c = img.crop(box[types])
    if (use_content==True)&(types=='srt'):
        width,_ = img_c.size
        img_c = generate_content_img(content,width,fontsize=fontsize)
    return img_c

def generate_content_img(content,width,fontsize=50):
    # 导入字体
    font = ImageFont.truetype('./fonts/msyhbd.ttc',fontsize)
    # 字幕间距
    srt_gap = 10
    w, h = font.getsize(content)
    # 背景图片
    bg = Image.new('RGB', (width, h+2*srt_gap ), color=(0,0,0))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(bg) 
    draw.text(((width-w)/2, srt_gap), content, fill="#00FFFF", font=font)  # #78e830 #00FFFF 
    draw = ImageDraw.Draw(bg,"RGB")
    return bg

def create_result(get_data,box_img_ratio = (0.0, 0.0, 1.0, 0.85),box_srt_ratio=(0.0, 0.85, 1.0, 0.95),use_content=False,fontsize=50):
    result_list = extract_data(get_data)
    # 获得 box 尺寸
    box_dict = get_img_size(result_list,box_img_ratio,box_srt_ratio)

    # 获得 裁剪的子图
    subs_imgs = [img_crop(img_name=d['img'],types=d['type'],box=box_dict,content=d['content'],use_content=use_content,fontsize=fontsize) for d in result_list]
    
    width_new = subs_imgs[0].size[0]
    height_new = sum([i.size[1] for i in subs_imgs])
    
    result_img = Image.new(subs_imgs[0].mode, (width_new,height_new))

    # 逐步高度
    h_params = 0
    for i, m in enumerate(subs_imgs):
        result_img.paste(m,box=(0,h_params))
        h_params += m.size[1]

    return result_img

