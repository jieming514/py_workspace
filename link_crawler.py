
## 爬取页面链接

import re
import urllib.request


def getlink(url):

    # 模拟浏览器
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                             " (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    # 根据需求构建好链接表达式
    pat = '(https?://[^\s";]+\.(\w|/)*)'
    links = re.compile(pat).findall(data)
    # 去重复
    return list(set(links))


url = "https://blog.csdn.net/"
linkList = getlink(url)
for link in linkList:
    print(link[0])
