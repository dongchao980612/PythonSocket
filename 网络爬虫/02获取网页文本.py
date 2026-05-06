# 导入库
import requests
from lxml import etree

# 发送请求
gushiwang_url = "https://www.yigushi.com/gushi/"
response = requests.get(gushiwang_url)

# 校验
if response.status_code == 200:
    print("发起爬虫请求成功", response.encoding)
    # print(response.text)

    # 解析本文
    tree = etree.HTML(response.text)

    titles = tree.xpath('//table//tr[1]/td[1]//strong')[0]
    print(titles.text)  # 儿童故事

    title_items = tree.xpath('//table//tr[1]/td[1]//li//a')
    for item in title_items:
        print(item.text)

    sub_page_urls = tree.xpath('//table//tr[1]/td[1]//li//a/@href')
    for url in sub_page_urls:
        sub_response = requests.get(url)
        if sub_response.status_code == 200:
            sub_response.encoding = sub_response.apparent_encoding
            tree = etree.HTML(sub_response.text)
            sub_title = tree.xpath("//h1[@class='title']")[0]
            print("子页面标题", sub_title.text)
            sub_content = tree.xpath("//div[@class='content']//text()")  # len = 46

            try:
                with open("./第一故事网/{}.txt".format(sub_title.text), "w", encoding="utf-8") as f:
                    for content in sub_content:
                        f.write(content+"\n")
                    print(sub_title.text + "保存成功")
            except Exception as e:
                print("保存失败...,原因是：", e)

else:
    print("发起爬虫请求失败")
