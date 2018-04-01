import re
import urllib.request
import requests
# 全程为get请求


for n in range(0, 1):
    url = 'http://www.htqyy.com/genre/musicList/3?pageIndex=%d&pageSize=20&order=hot' % n
    html = requests.get(url)
    # print(html.text)
    data_url = (re.findall('value="(.*?)"><span', html.text))
    for m in data_url:
        data_title_list = (re.findall(
            '</span><span class="title"><a href="/play/%s" target="play" title="(.*?)"' % m, html.text))
        url2 = 'http://f1.htqyy.com/play6/%s/mp3/2' % m

        data_title_str = (''.join(data_title_list))
        # ''.join() 作用为列表转换为字符串
        print(data_title_str)
        print(url2)
        urllib.request.urlretrieve(url2, 'C:\\Users\LIYANG\Desktop\新建文件夹\\%s.mp3' % data_title_str)