# 导入库
import requests
from lxml import etree

# 发送请求
gushiwang_url = "https://www.yigushi.com/gushi/"
response = requests.get(gushiwang_url)

# 校验
print(response)
if response.status_code == 200:
    print("发起爬虫请求成功", response.encoding)
    response.encoding=response.apparent_encoding
    tree = etree.HTML(response.text)
    title = tree.xpath('//table//tr[1]/td[1]//strong/text()')[0]
    print(title)

    title_items = tree.xpath('//table//tr[1]/td[1]//li//a')
    sub_page_urls = tree.xpath('//table//tr[1]/td[1]//li//a/@href')
    print(sub_page_urls[0])
else:
    print("发起爬虫请求失败")
