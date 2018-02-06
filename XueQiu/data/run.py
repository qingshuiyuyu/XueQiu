#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:chen_yakun
@file: run.py 
@time: 2018/02/06
"""

from scrapy import cmdline
cmdline.execute("scrapy crawl discover".split())