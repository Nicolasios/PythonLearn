
import re
import time
import asyncio
import requests
import numpy

url = 'https://www.sbiquge.com/3_3983/'
response = requests.get(url)
response.encoding = 'gbk'
html = response.text
source = re.findall(r'<dd>.*</dd>',html,re.S)[0]
title = re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html)[0]
fb = open('%s.txt' % title,'w',encoding="gbk")

chapter  = re.findall(r'href ="(.*?)">(.*?)</a>',source)
chapter = numpy.array(chapter)
async def main(chapter_info):
    chapter_url,chapter_title = chapter_info
    chapter_url = "https://www.sbiquge.com" + chapter_url
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = "gbk"
    chapter_html = chapter_response.text
    #写入标题
    fb.write(chapter_title)
    fb.write('\n')
    chapter_content = re.findall(r'/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;([\S]+)',chapter_html)
    chapter_content = numpy.array(chapter_content)
    #写入章节内容
    for chapter_content_1 in chapter_content:
        fb.write(chapter_content_1)
        fb.write('\n')
    
def launch():
    for chapter_info in chapter[6:10]:
        asyncio.get_event_loop().run_until_complete(main(chapter_info))
        
if __name__ == '__main__':
    tick1 = time.time()

    asyncio.run(launch())

    tick2 = time.time()
    print("异步时间",tick2-tick1 %"s")