# _*_ coding: utf-8 _*_
from telegraphapi import Telegraph
import requests
from bs4 import BeautifulSoup
import ast

author_name = "@JKearnsl"
author_url = "https://t.me/JKearnsl"

html = requests.get("https://allhentai.ru/list/genre/trap?sortType=updated")
items = BeautifulSoup(html.content, features="html.parser").find("div",class_="tiles row")
link = "https://allhentai.ru"+items.contents[1].contents[5].contents[7].contents[1].attrs['href']+"/vol1/1"
html_cont = requests.get(link)
pics = BeautifulSoup(html_cont.content, features="html.parser").find("div", class_="pageBlock container reader-bottom").find("script",type="text/javascript").contents[0][120:]
pics = pics[pics.find("[['"):]
links = ast.literal_eval("{1:"+pics[:pics.find("{")-14]+']'+"}")[1]
picURL = ''
for link in links:
    picURL=picURL+ "<img src='"+"https:"+link[0]+link[2][:link[2].find("?")]+"'><figcaption></figcaption>" # ссылка на картинку в <img src='PICURL'>
tag_list = ''
print(picURL)
for i in items.find("div", class_="tile-info").contents:
    try:
        tag_list = tag_list + " #"+i.contents[0]
    except:
        pass

print(items.contents[1].contents[5].contents[9].attrs['title'])
print(items.contents[1].contents[5].contents[7].contents[1].attrs['title'])
print(tag_list)
telegraph = Telegraph()

telegraph.createAccount("PythonTelegraphAPI")
page = telegraph.createPage(items.contents[1].contents[5].contents[7].contents[1].attrs['title'], html_content="<b>"+items.contents[1].contents[5].contents[9].attrs['title']+"</b><h4>"+tag_list+"</h4>"+picURL,author_name=author_name,author_url=author_url)

print('http://telegra.ph/{}'.format(page['path']))
