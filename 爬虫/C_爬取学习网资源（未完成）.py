import urllib.request
# 在PY2中为 urllib2
import http.cookiejar


cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)


def login():

    req = urllib.request.Request('https://www.ks5u.com/user/inc/UserLogin_Index.asp',
                                  data=bytes('username=15170266881&password=ly19980911&c_add=0',
                                             encoding='utf8'))
    html = opener.open(req).read()
    return html


if bytes('15170266881', encoding='utf8') in login():
    print('登录成功')
else:
    print('登录失败')


def getlist():
    req = urllib.request.Request('https://www.ks5u.com/so/search.asp?',
                                 data=bytes('subject_value=1&'
                                            'grade_value=0&'
                                            'type_value=7&'
                                            'stype_value=8&'
                                            'source_value=0&'
                                            'edition_value=0&'
                                            'beikeedition_value=0&'
                                            'bixiu_value=0&'
                                            'danyuan_value=0&'
                                            'keshi_value=0&'
                                            'searchtype=0&'
                                            'ordertype=0&'
                                            'q=&bk=0', encoding='utf8'))
    return opener.open(req).read()
print (getlist())
