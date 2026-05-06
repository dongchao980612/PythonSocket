# 导入库

from lxml import etree
import requests

# 发送请求
gushiwang_url = "https://www.yigushi.com/gushi/search.php"

# data = input("请输入关键词：")
data = "小马"
params = {
    "kw": data,
    "page": 2
}
response = requests.get(gushiwang_url, params)
print(response.url)
# 校验
if response.status_code == 200:
    print("发起爬虫请求成功", response.encoding)
    # print(response.text)
    tree = etree.HTML(response.text)
    sub_urls = tree.xpath("//div[@class='catlist']/ul//a/@title")
    print(sub_urls)
else:
    print("发起爬虫请求失败")
