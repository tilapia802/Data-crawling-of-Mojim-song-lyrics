# Data-crawling-of-Mojim-song-lyrics   
Python script that helps you download song lyrics you want from Mojim.com.      
### Get URL of all the songs of a singer
```
python GetUrl.py url_of_singer
```
For example, if you want to download all the song URL in Mojim.com of singer "梁靜茹".
```
python GetUrl.py https://mojim.com/twh100095-A2.htm
```
After execution the script, you will see 2 files in the directory, which are WebsiteList and SongList.
In WebsiteList, you can see all the song URL in Mojim.com of singer "梁靜茹".
```
https://mojim.com/twy100593x3x9.htm
https://mojim.com/twy100593x9x1.htm
https://mojim.com/twy100593x8x20.htm
```
In SongList, you can see coresponding song name of the song URL.
```
我想我不會愛你 歌詞
愛著愛著就永遠 歌詞
你快樂未必我快樂 歌詞
```
### Get song lyrics in WebsiteList
```
python GetSongLyrics.py WebsiteList 20
```
Here 20 means crawling from line 20 of WebsiteList, so you don't need to crawl data from start of WebsiteList every time. 
