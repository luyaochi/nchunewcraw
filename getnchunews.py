#!/usr/bin/python
#coding:utf-8
import urllib,re

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
nchuNews = client.nchuNews

nchuNewsList = nchuNews.nchuNewsList


main_path = 'http://www.nchu.edu.tw/'
path = main_path + 'news.php?type=1&id='+ '2' +'&page=' + '0'
data = urllib.urlopen(path)
content = data.read().decode('utf8', 'ignore')
#content = content[content.find('<div id="ind-news">'):content.find('<div class="page1">')]
#title_pattern = re.compile('<h5>(.+?)</h5>', re.S)

date_pattern = re.compile('<span class="date-right">(.+?)</span>')
info_pattern = re.compile('<a href="(.+?)">(.+?)</a>')

#content = title_pattern(content)
date = date_pattern.findall(content)
info = info_pattern.findall(content)
for i in range(len(date)):
	print date[i]
	print main_path + info[i][0]
	print info[i][1]
	#nchuNews.collection.insert({"date":date[i],"title":info[i][1],"url":main_path + info[i][0]})

info[0][1]
#import os
#os.system("pause")
