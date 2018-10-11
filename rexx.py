# Filename: rexx.py

# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import re
import sys
import time

# reload(sys)
# sys.setdefaultencoding("utf-8")

def spider(url):
    print (url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    html = requests.get(url, headers=headers) #伪装成浏览器
    selector = etree.HTML(html.text) #将网页html变成树结构，用于xpath
    content = selector.xpath('//figure[@class="post-image "]') #提取figure标签
    for each in content:
        tmp = each.xpath('a/img/@src')#把img标签的src属性提取出来
        pic = requests.get(tmp[0])#访问图片
        print ('downloading: ' + tmp[0])
        string = re.search('\d+/\d+/(.*?)\\.jpg', str(tmp[0])).group(1) #正则表达式匹配图片名字
        fp=open('pic2\\'+string+'.jpg','wb')#放到pic2文件夹内，要自己创建
        fp.write(pic.content)
        fp.close
if __name__ == '__main__':
    pool = ThreadPool(2) #双核电脑
    tot_page = []
    for i in range(1,11): #提取1到10页的内容
        link = 'http://hotpics.cc/page/' + str(i)
        tot_page.append(link)
    pool.map(spider, tot_page)#多线程工作
    pool.close()
    pool.join()

# # ####################################################################
# import re
# import urllib.request
# from multiprocessing.dummy import Pool as ThreadPool
# import sys,os
#
#
# # ------ 获取网页源代码的方法 ---
# def getHtml(url):
#     page = urllib.request.urlopen(url)
#     html = page.read()
#     return html
#
#
# # # ------ getHtml()内输入任意帖子的URL ------
# # # html = getHtml("https://tieba.baidu.com/p/5352556650")
# # html = getHtml("http://hotpics.cc/page/6")
# # # ------ 修改html对象内的字符编码为UTF-8 ------
# # html = html.decode('UTF-8')
#
#
# # ------ 获取帖子内所有图片地址的方法 ------
# def getImg(html):
#     # ------ 利用正则表达式匹配网页内容找到图片地址 ------
#     reg = r'src="([.*\S]*\.jpg)"'
#     imgre = re.compile(reg);
#     imglist = re.findall(imgre, html)
#     return imglist
#
#
# def getUrlHtml(urls):
#     imgName = 0
#     for url in urls:
#         html = getHtml(url)
#         html = html.decode('UTF-8')
#         imgList = getImg(html)
#         for imgPath in imgList:
#             # ------ 这里最好使用异常处理及多线程编程方式 ------
#             try:
#                 f = open(sys.path[0] +"/pics/"+ str(imgName) + ".jpg", 'wb')
#                 f.write((urllib.request.urlopen(imgPath)).read())
#                 print(imgPath)
#                 f.close()
#             except Exception as e:
#                 print(imgPath + " error")
#             imgName += 1
#
#
# def main():
#     #pool = ThreadPool(2)  # 双核电脑
#     tot_page = []
#     # for i in range(1, 11):  # 提取1到10页的内容
#     #     link = 'http://hotpics.cc/page/' + str(i)
#     #     tot_page.append(link)
#     tot_page.append('https://tieba.baidu.com/p/5352556650');
#
#     getUrlHtml(tot_page)
#     #pool.map(getUrlHtml, tot_page)  # 多线程工作
#     #pool.close()
#     #pool.join()
#
#
# if __name__ == '__main__':
#     main()

##################################################################################
