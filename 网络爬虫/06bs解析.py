from bs4 import BeautifulSoup

import requests

# 发送请求
gushiwang_url = "https://www.yigushi.com/gushi/"
response = requests.get(gushiwang_url)

# 校验
if response.status_code == 200:
    print("发起爬虫请求成功", response.encoding)
    soup = BeautifulSoup(response.text, features='lxml')

    div_element = soup.find("div", class_="head-txt").find("strong")
    title = div_element.getText()
    print(title)  # 儿童故事

    title_items = soup.find("div", class_="list-txt").find_all("a")
    for item in title_items:
        print(item.text, item.attrs["href"])

else:
    print("发起爬虫请求失败")
