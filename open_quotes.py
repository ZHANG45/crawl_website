# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 13:21:21 2018

@author: Mac
"""
import os
import json


file_name = 'quotes.json'

os.system("scrapy crawl quotes -o " + file_name)

with open(file_name) as f:
    load = json.load(f)
print(load)