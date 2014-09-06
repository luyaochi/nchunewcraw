#!/usr/bin/python
#coding:utf-8
import re
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
nchuNews = client.nchuNews
nchuNewsContents = nchuNews.Contents

div_pattern = re.compile('<font(.+?)</',re.S)

for nchuNewsContentitem in nchuNewsContents.find({},{"_id":0}):
	div = div_pattern.findall(nchuNewsContentitem['content'])
	for a in div:
		print a
	break