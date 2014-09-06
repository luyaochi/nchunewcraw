#!/usr/bin/python
#coding:utf-8

import urllib,re

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
nchuNews = client.nchuNews
nchuNewsList = nchuNews.nchuNewsList

itemsIDs = range(1,8)
itemsNames = ['一般新聞','興新聞','榮譽榜','研討會。演講','獎學金。貸款','招生。徵才。就業','活動消息']
CurrentNum = []

main_path = 'http://www.nchu.edu.tw/'

if nchuNewsList.find({}).count() == 0:
	for i in range(7):
		path = main_path + 'news.php?type=1&id='+ str(itemsIDs[i]) +'&page=0'
		data = urllib.urlopen(path)
		content = data.read().decode('utf8', 'ignore')
		total_pattern = re.compile('<font color="#999999">(.+?)</font>')
		totalNum = total_pattern.findall(content)
		totalNum = totalNum[0][1:len(totalNum[0])-4]
		totalNumSplit = totalNum.split(',')
		num = len(totalNumSplit)
		if num > 1:
			totalNumSplit = int(float(totalNumSplit[0]+totalNumSplit[1])) 
			totalNumSplit = totalNumSplit - totalNumSplit%20
		else:
			totalNumSplit = int(float(totalNumSplit[0]))
			totalNumSplit = totalNumSplit - totalNumSplit%20
		CurrentNum = totalNumSplit
		nchuNews.nchuNewsList.insert({"itemsNames":itemsNames[i],"itemsIDs":itemsIDs[i],"CurrentNum":CurrentNum,"totalNumSplit":totalNumSplit})
		print itemsNames[i]
		print itemsIDs[i]
		print totalNumSplit
client.close()
