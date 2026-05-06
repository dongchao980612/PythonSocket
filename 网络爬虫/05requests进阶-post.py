# 导入库

from lxml import etree
import requests

# 发送请求
baidufanyi_url = "https://fanyi.baidu.com/sug"

data = {
    "kw": "大学生",
}
response = requests.post(baidufanyi_url, data)
# 校验
if response.status_code == 200:
    print("发起爬虫请求成功", response.encoding)
    data = response.json()["data"]
    # print(data)
    for i in data:
        print("中文：", i["k"], "\t英文释义", i["v"])
else:
    print("发起爬虫请求失败")
