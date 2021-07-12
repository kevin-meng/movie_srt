# -*- coding:utf8 -*- 
import os,pickle

def dump_pickle(file,dir):
    """
    cannot serialize a bytes object larger than 4 GiB
    """
    with open(dir,'wb') as f:
        pickle.dump(file,f,protocol=4)

def load_pickle(dir):
    with open(dir,'rb') as f:
        out_file = pickle.load(f)
    return out_file

def check_path(movie_name):
    
    for d in ['','srt','movie','imgs','result']:
        p = f"../data/{movie_name}/{d}"
        if not os.path.exists(p):
            os.mkdir(p)     