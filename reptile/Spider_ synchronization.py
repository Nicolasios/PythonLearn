import requests
import re
import numpy
import time

tick2 = time.time()

url = 'https://book.qidian.com/info/1264634#Catalog'

response = requests.get(url)

response.encoding = 'gbk'


html = response.text

source = re.findall(r'<dd>.*</dd>',html,re.S)[0]

title = re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html)[0]
fb = open('%s.txt' % title,'w',encoding="gbk")



chapter  = re.findall(r'href ="(.*?)">(.*?)</a>',source)
chapter = numpy.array(chapter)
print(chapter.shape)
for chapter_info in chapter[6:10]:
    chapter_url,chapter_title = chapter_info
    chapter_url = "https://vipreader.qidian.com/charpter/" + chapter_url
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = "gbk"
    chapter_html = chapter_response.text
    fb.write(chapter_title)
    fb.write('\n')
    chapter_content = re.findall(r'/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;([\S]+)',chapter_html)
    chapter_content = numpy.array(chapter_content)

    for chapter_content_1 in chapter_content:
        fb.write(chapter_content_1)
        fb.write('\n')
fb.close()
tick1 = time.time()
print("同步时间:",tick1-tick2,'s')