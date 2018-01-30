# This is a program for you to get lyrics you want on https://mojim.com/ (Mojim.com)
# The usage of this program:
# 1.Put all the url that you want to download in a file(one in a line), you can also refer to the sample WebsiteList provided under the same directory 
# 2.Type the command: $ python GetSongLyrics.py WebsiteList 
# 3.After the program finish downloading the data, you will see all the lyrics you want,the order is the same as your WebsiteList.
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs

def GetUrlLyrics(url,id):
	r = requests.get(url,verify=False)
	content = r.text
	soup = BeautifulSoup(content,'html.parser')
	print "Getting lyrics from " + url
	filename = "lyrics" + str(id)
	file_w = codecs.open(filename,'w','utf-8')
	flag = 0
	for line in soup.find_all('br'):
		next = line.nextSibling
		if not (next and isinstance(next,NavigableString)):
			continue
		next2 = next.nextSibling
		if next2 and isinstance(next2,Tag) and next2.name == 'br':
			text = str(next).encode('utf-8').strip()
			if text:
				if next.encode('utf-8')[0] == '[':
					file_w.write(next.encode('utf-8')+"\n")
					flag = 1
				else:
					continue
	if flag==0:
		file_w.write("This song's format is not supported.\n")
	file_w.close
	return 					

id=0
file = open(sys.argv[1],'r')
while True:
	line = file.readline()
	if not line:
		break
	id = id + 1
	if id>= int(sys.argv[2]):
		print "---------------------------------------"
		print line	
		GetUrlLyrics(line,id)		
file.close
				




