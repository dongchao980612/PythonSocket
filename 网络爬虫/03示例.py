# 导入库
import requests
from lxml import etree

# 发送请求
xuanyuyueduwang_url = "https://www.xyyuedu.com/etdw/zhongguominjiangushi/index.html"
response = requests.get(xuanyuyueduwang_url)
BASE_URL = "https://xyyuedu.com"
print(response.status_code)
if response.status_code == 200:
    print("发起爬虫请求成功", response.encoding)
    # print(response.text)

    tree = etree.HTML(response.text)
    sub_urls = tree.xpath("//ul[@class='zhangjie2']//@href")

    for url in sub_urls:
        print(BASE_URL + url)

        sub_response = requests.get(BASE_URL + url)
        if sub_response.status_code == 200:
            sub_response.encoding = sub_response.apparent_encoding
            tree = etree.HTML(sub_response.text)
            sub_title = tree.xpath("//div[@id='arcxs_title']/h1/text()")[0]
            # print(sub_title)
            sub_content = tree.xpath("//div[@class='onearcxsbd']//text()")
            # print(sub_content)

            try:
                with open("./轩宇阅读网/{}.txt".format(sub_title), "w", encoding="utf-8") as f:
                    for content in sub_content:
                        if '\r\n' not in content:
                            # print(content)
                            f.write(content + "\n")
                    print(sub_title + "保存成功")
            except Exception as e:
                print("保存失败...,原因是：", e)



else:
    print("发起爬虫请求失败")
