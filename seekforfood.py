#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:23:35 2020

@author: raymondwang
"""

# 0 西一1楼/1 西一二楼/2 西二2楼/3 东一一楼/4 东一二楼/5 东三/6 百景园1楼/7 百景园二楼/8 集贤楼/9 集锦园/
import numpy as np
from PIL import Image, ImageDraw, ImageFont

candidates=["西一1楼"," 西一二楼", "西二2楼", "东一1楼","东一2楼", "东三","百景园1楼","百景园2楼","集贤楼","集锦园"]

canteen=candidates[np.random.randint(0, high=10)]
#print(canteen)

image=Image.new('RGB',(400,400),(255,255,255))
#选择文字字体和大小
setFont = ImageFont.truetype('C:/Windows/Fonts/STXINGKA.TTF', 60)
#设置文字颜色
fillColor = "#0000ff"   #蓝色
size=(40,40)
#新建绘图对象
draw = ImageDraw.Draw(image)
#显示图片
draw.text((100,180),canteen,font=setFont,fill=fillColor,direction=None)
image.show()






