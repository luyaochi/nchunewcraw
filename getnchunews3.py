#!/usr/bin/python
#coding:utf-8
import urllib,re

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
nchuNews = client.nchuNews
nchuNewsList = nchuNews.nchuNewsList
nchuNewsContentList = nchuNews.nchuNewsContentList

CurrentNum = 0
totalNum = 0

for nchuNewsitem in nchuNewsList.find({},{'_id':0}):
	for x in  nchuNewsitem:
		if x == 'itemsIDs':
			itemsIDs = nchuNewsitem[x]
		elif x == 'CurrentNum':
			CurrentNum = nchuNewsitem[x]
		elif x == 'totalNumSplit':
			totalNum = nchuNewsitem[x]
		elif x == 'itemsNames':
			itemsName = nchuNewsitem[x]
		else:
			pass

		main_path = 'http://www.nchu.edu.tw/'
		for i in range(CurrentNum-2,CurrentNum):
			path = main_path + 'news.php?type=1&id='+ str(itemsIDs) +'&page=' + str(i)
			data = urllib.urlopen(path)
			content = data.read().decode('utf8', 'ignore')
			content_pattern = re.compile('<div id="ind-news">(.+?)</div>', re.S)
			date_pattern = re.compile('<span class="date-right">(.+?)</span>')
			info_pattern = re.compile('<a href="(.+?)">(.+?)</a>')

			content = content_pattern.findall(content)[0]
			date = date_pattern.findall(content)
			info = info_pattern.findall(content)

			for i in range(len(date)):
				if nchuNews.nchuNewsContentList.find({"newstitle":info[i][1]}).count() == 0:
					nchuNews.nchuNewsContentList.insert({"date":date[i],"url":main_path + info[i][0],"newstitle":info[i][1]})
					print date[i]
					print main_path + info[i][0]
					print info[i][1]

		CurrentNum = CurrentNum-2
		print CurrentNum
client.close()
