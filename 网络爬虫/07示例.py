from bs4 import BeautifulSoup

import requests

# 发送请求
gushiwang_url = "https://www.xyyuedu.com/etdw/zhongguominjiangushi/index.html"
response = requests.get(gushiwang_url)
BASE_URL = "https://xyyuedu.com"
# 校验
if response.status_code == 200:
    print("发起爬虫请求成功", response.encoding)
    response.encoding=response.apparent_encoding
    soup = BeautifulSoup(response.text, features='lxml')

    a_element = soup.find("ul", class_="zhangjie2").find_all("a")
    # print(a_element)
    for i in a_element:
        # print(i.text,BASE_URL+i.attrs["href"])
        res=requests.get(BASE_URL+i.attrs["href"])
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, features='lxml')
        txt = soup.find("div",class_="onearcxsbd").text
else:
    print("发起爬虫请求失败")
