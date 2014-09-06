#!/usr/bin/python
#coding:utf-8
import re
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
nchuNews = client.nchuNews
nchuNewsContents = nchuNews.Contents

title_pattern = re.compile('<table border="0" align="right" cellpadding="0" cellspacing="8">(.+?)</table>', re.S)
info_pattern = re.compile('<table width="100%" border="0" cellpadding="0" cellspacing="1" class="t0">(.+?)</table>', re.S)
tr_pattern = re.compile('<tr>(.+?)</tr>',re.S)
td_pattern = re.compile('<td>(.+?)</td>',re.S)
span_pattern = re.compile('/></span>(.+?)</td>')

td_pattern = re.compile('<td class="t2">(.+?)</td>',re.S)

div_pattern = re.compile('size=4>(.+?)</',re.S)


for nchuNewsContentitem in nchuNewsContents.find({},{"_id":0}):
	title = title_pattern.findall(nchuNewsContentitem['content'])[0]
	title = tr_pattern.findall(title)[0]
	title = span_pattern.findall(title)
	print 'updatetime:' + title[0]
	print 'posttime:' + title[1]
	info = info_pattern.findall(nchuNewsContentitem['content'])
	info = tr_pattern.findall(info[0])

	td = td_pattern.findall(info[0])
	unit = td[0]
	poster = td[1]

	td = td_pattern.findall(info[1])
	classes = td[0]
	source = td[1]

	div = div_pattern.findall(nchuNewsContentitem['content'])
	


#11111111111111111
	source = source.split('\t')
	a = ''
	for x in source:
		if len(x) > len(a):
			a = x

	source = a
	source = source.split(' ')
	a = ''
	for x in source:
		if len(x) > len(a):
			a = x
	source = a
#111111111111111111111
	unit = unit.split('\t')
	a = ''
	for x in unit:
		if len(x) > len(a):
			a = x

	unit = a
	unit = unit.split(' ')
	a = ''
	for x in unit:
		if len(x) > len(a):
			a = x
	unit = a

#111111111111111111111


	print div
	print unit
	print poster
	print classes
	print source
	#nchuNews.test.insert({"unit":unit,"poster":poster,"classes":classes,"source":source,"updatetime":title[0],"posttime":title[1]})	
	break 



client.close()
