
import urllib.request
import urllib.error

'''
file = urllib.request.urlopen("http://www.baidu.com")

data = file.read()
# dataline = file.readline()

# 将读取的网页信息写入本地
fhandle = open("D:\\work\\py_workspace\\rescue\\1.html","wb")
fhandle.write(data)
fhandle.close()

# filename = urllib.request.urlretrieve("https://www.imooc.com/", filename="D:\\work\\py_workspace\\rescue\\2.html")
# urllib.request.urlcleanup()

# 设置请求头
url = "https://www.oschina.net/"
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                         "(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")

opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fhandle2 = open("D:\\work\\py_workspace\\rescue\\2.html","wb")
fhandle2.write(data)
fhandle2.close()


# 抽取函数
def url_read(url):
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                             "(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read()
    return data


data = url_read("https://www.csdn.net/")
fhandle3 = open("D:\\work\\py_workspace\\rescue\\3.html","wb")
fhandle3.write(data)
fhandle3.close()

'''


# 超时设置
for i in range(1, 5):
    try:
        file = urllib.request.urlopen("https://www.oschina.net/")
        data = file.read()
        print(len(data))
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
# print(str(e.code) + "--" + e.reason)

