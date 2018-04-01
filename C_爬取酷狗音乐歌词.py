# 最后修改时间：2018 02 19
# 下载酷狗里面的歌子有加密，未能成功完成

import requests
import re
# import urllib.request


def dow_lyc(singer_id):

    i = 0  # 初始化列表的下标
    url_lyc_list = []  # 创建空列表用于保存歌词的链接

    url_singer = 'http://www.kugou.com/yy/singer/home/%s.html' % (singer_id )
    html = requests.get(url_singer)
    hash_singer_date_list = re.findall(r'value="(.*?) /><span title="分享"', html.text)
    song_id_list = re.findall(r'"album_id":(.*?),"', html.text)

    hash_singer_date_str = (''.join(hash_singer_date_list))

    hash_singer_date1_list = hash_singer_date_str.split('|')    # 按照指定分隔符分割字符串
    # print(hash_singer_date1_list, end='\n\n')
    print('歌曲ID个数为：' + str(len(song_id_list)), end='\n\n')
    with open('C:\\Users\\LIYANG\\Desktop\\date.txt', 'w')as f:

        for n in range(1, len(hash_singer_date1_list), 2):
            print('\n第' + str(n//2+1) + '首歌', end='\n')
            f.write('第' + str(n//2+1) + '首歌' + '\n')
            if(n == 1):
                print(hash_singer_date1_list[n-1].split('"')[0])
                f.write('歌名：\t' + hash_singer_date1_list[n-1].split('"')[0] + '\n')
            else:
                print(hash_singer_date1_list[n-1].split('"')[1])
                f.write('歌名：\t' + hash_singer_date1_list[n-1].split('"')[1] + '\n')
            print(hash_singer_date1_list[n])
            f.write('hash码：' + hash_singer_date1_list[n] + '\n')

            temp = 1

            while(temp == 1):
                print(song_id_list[i])
                f.write('ID：\t' + song_id_list[i] + '\n')
                url_play = 'http://www.kugou.com/song/#hash=%s&album_id=%s' \
                           % (hash_singer_date1_list[n], song_id_list[i])
                print(url_play)
                # urllib.request.urlretrieve(url_play, 'C:\\Users\LIYANG\Desktop\新建文件夹\\%s.mp3' % (n))
                url_lyc = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash=%s&album_id=%s&_=1518976378036' \
                          % (hash_singer_date1_list[n], song_id_list[i])
                print(url_lyc)

                url_lyc_list.append(url_lyc)

                f.write('链接为：' + url_play + '\n\n')
                temp = 0
                i += 1
                if(i == len(song_id_list)):
                    break
    print(len(url_lyc_list))
    f.close()
    with open('C:\\Users\\LIYANG\\Desktop\\歌词.txt', 'a', encoding='utf-8')as f:
        for n in url_lyc_list:
            html = requests.get(n)
            # print(html.text)
            lyc_list = re.findall(r'"lyrics":"(.*?)","author_id"', html.text)
            # print(lyc_list)
            lyc_str = (''.join(lyc_list))
            # Unicode转码为中文方法
            print(lyc_str.encode('utf-8').decode('unicode_escape'))
            f.write(lyc_str.encode('utf-8').decode('unicode_escape') + '\n\n')
    f.close()


dow_lyc(722869)
