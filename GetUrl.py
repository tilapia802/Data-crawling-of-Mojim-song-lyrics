# This is a program for you to get URL of all the song of a singer you want on https://mojim.com/ (Mojim.com)
# The usage of this program:
# 1.Type the command: $ python GetSongLyrics.py URL_of_singer_song_list 
# 2.After the program finish downloading the data, you will see all the URL in WebsiteList.

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs

file_w = codecs.open("WebsiteList",'a','utf-8')
file_w2 = codecs.open("SongList",'a','utf-8')

r = requests.get(sys.argv[1],verify=False)
content = r.text
soup = BeautifulSoup(content,'html.parser')
for line in soup.find_all('a',href=True):
	if(line['href'][:4] == "/twy"):
		file_w2.write(line['title'].encode('utf-8')+"\n")
		file_w.write("https://mojim.com"+line['href']+"\n")

file_w.close
file_w2.close
				


				




