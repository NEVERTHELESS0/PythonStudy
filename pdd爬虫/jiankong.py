import requests
import re
import xlrd
import xlwt

def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_page(html):
    pattern = re.findall('<span class="g-sales false">已拼(.*?)件</span>', html)
    pattern2 = re.findall('<span class="g-group-price false"><i class="false">￥</i>(.*?)</span>', html)
    pattern3 = re.findall('<span class="enable-select">(.*?)</span>', html)
    print(pattern)
    print(pattern2)
    print(pattern3)

def read_excel(filename):
    workbook = xlrd.open_workbook(filename)
    sheet1 = workbook.sheet_by_index(0)
    print(sheet1.name, sheet1.ncols, sheet1.nrows)
    test = [[0 for i in range(sheet1.ncols)] for j in range(sheet1.nrows)]
    for i in range(0, sheet1.nrows ):
        for j in range(0, sheet1.ncols):
            test[i][j] = sheet1.cell(i, j).value
    print(test)
    return test

def change_excel(filename, text):
    text[0].append(10)
    text[1].append(10)
    text[2].append(10)

    print(text)
    return text
def save_excel(filename, test, col, row):
    rb = xlwt.Workbook()
    sheet = rb.add_sheet(u'sheet1')
    for i in range(0, col):
        for j in range(0, row):
            sheet.write(i, j, test[i][j])
    rb.save(filename)

def main():
    url = 'http://mobile.yangkeduo.com/goods2.html?goods_id=2567419373'
    html = get_page(url)
    print(html)

    text = change_excel('123.xls', read_excel('123.xls'))
    save_excel('123.xls', text, 3 ,4)
if __name__ == '__main__':
    main()