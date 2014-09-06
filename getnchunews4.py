#!/usr/bin/python
#coding:utf-8
import urllib,re

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
nchuNews = client.nchuNews
nchuNewsList = nchuNews.nchuNewsList
nchuNewsContentList = nchuNews.nchuNewsContentList
nchuNewsContents = nchuNews.Contents
for nchuNewsitem in nchuNewsContentList.find({},{"url":1,"_id":0}):
	for index  in nchuNewsitem:
		path = nchuNewsitem[index]
		data = urllib.urlopen(path)
		content = data.read().decode('utf8', 'ignore')
		nchuNews.Contents.insert({"content":content})
		print content
client.close()