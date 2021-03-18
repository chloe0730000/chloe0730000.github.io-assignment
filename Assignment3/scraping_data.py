#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:12:23 2021

@author: cchou
"""


import requests
import pandas as pd
import re


address = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json'
json_res = requests.get(address).json()
data = pd.DataFrame(json_res["result"]["results"])
res = data[["stitle", "longitude", "latitude", "file"]]

res["file"] = res["file"].apply(lambda x: x.split("http://")[1:])
res["file"] =  res["file"].apply(lambda x: ["http://"+item for item in x][0])

res.to_csv('/Users/cchou/Documents/GitHub/Random/Software Eng Training/Assignment3/output.txt', 
           header=False, index=False, sep=',', mode='a')
