import urllib,re

main_path = 'http://www.nchu.edu.tw/'
path = main_path + 'news.php?type=1&id=1&page=0'
data = urllib.urlopen(path)
content = data.read().decode('utf8', 'ignore')
content_pattern = re.compile('<div id="ind-news">(.+?)</div>', re.S)
date_pattern = re.compile('<span class="date-right">(.+?)</span>')
info_pattern = re.compile('<a href="(.+?)">(.+?)</a>')
content = content_pattern.findall(content)[0]
date = date_pattern.findall(content)
info = info_pattern.findall(content)
for i in range(len(date)):
	print date[i]
	print main_path + info[i][0]
	print info[i][1]