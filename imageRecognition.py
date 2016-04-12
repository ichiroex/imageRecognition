# -*- coding: utf-8 -*-
# implemented by ichiroex
# other codes are also available on GitHub (https://github.com/ichiroex)

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import json
import time 
import urllib
import re
import sys
import argparse

#画像データを投げて、カテゴリの候補上位5つを取得 (カテゴリ認識)
def getImageCategory(fname, modelName):

    register_openers()
    
    APIKEY = "(APIKEY)"
    url = 'https://api.apigw.smt.docomo.ne.jp/imageRecognition/v1/concept/classify/?APIKEY=' + APIKEY
    
    f = open(fname, 'r')

    datagen, headers = multipart_encode({"image": f, 'modelName': modelName})
    request = urllib2.Request(url,datagen, headers)
    response = urllib2.urlopen(request)
    
    res_dat = response.read()
   
    #return candidate list
    return json.loads(res_dat)['candidates']


if __name__ == '__main__':
    
    # 引数 (オプション設定)
    parser = argparse.ArgumentParser()
    parser.add_argument('--image'    , dest='image', type=str, default='rose.jpg', help='name of input image')
    parser.add_argument('--model'    , dest='model', type=str, default='scene', help='modelName = {scene, fashion_pattern, fashion_type, fashion_style, fashion_color, food, flower, kinoko}')

    args = parser.parse_args()
    
    # 画像ファイル名, modelName の設定
    fname = args.image
    model_name = args.model
    
    # カテゴリ候補の取得 (カテゴリ認識を利用)
    candidate_list = getImageCategory(fname, model_name)
    
    # カテゴリのタグとスコアを表示
    for can in candidate_list:
        print can['tag'], can['score']
