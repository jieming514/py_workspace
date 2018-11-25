import re  # 正则表达式引用包
import urllib.request  # 网络引用包
import urllib.error


# 图片爬虫

def img_craw(url, page=1):
    html = urllib.request.urlopen(url).read()
    html = str(html)

    pat1 = '<div class="m-list".+?<div class="m-aside">'
    result = re.compile(pat1).findall(html)

    if len(result) == 0:
        return
    result = result[0]
    print(result)
    pat2 = '<img width="200" height="200" data-img="1" src="//(.+?\.jpg)"'
    imagelist = re.compile(pat2).findall(result)
    print(imagelist)
    x = 1
    for imageurl in imagelist:
        imagename = "D:/work/py_workspace/image/" + str(page) + str(x) + ".jpg"
        imageurl = "http://" + imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
        x += 1


for i in range(1, 50):
    '''
        url = "https://search.jd.com/Search?keyword=%E5%8F%B0%E5%BC%8F%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2" \
          "=671&page=" + str(i * 2 + 1) + "&s=" + str(53 * i) + "&click=0"
    '''
    url = "https://list.jd.com/list.html?cat=1713,3263,4761&ev=1000000001_102&page="\
          +str(i)+"&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main "
    img_craw(url, i)
