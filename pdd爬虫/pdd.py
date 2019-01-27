from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlwt
import xlrd
import datetime

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def login():
    browser.get('https://mms.pinduoduo.com/Pdd.html#/login')
    userName = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#usernameId"))
    )
    passWord = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#passwordId"))
    )
    VerificationCode = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#tuxing"))
    )
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#tuxing"))
    )
    userName.send_keys("15870800122")
    passWord.send_keys("lzg15870800122@")
    VerificationCode.send_keys(input("\n请输入验证码:"))
    browser.find_element_by_css_selector('#loginBtnId').click()
    if (wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#top-content > div.pdd-top-nav > div > a.pdd-logo"))
    )):
        print('成功登陆')


def getshuju():
    browser.get('https://mms.pinduoduo.com/Pdd.html#/directional/project?from=0')
    date = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "#direact_extension_project > table > tbody > tr:nth-child(2) > td:nth-child(6)"))
    )
    return date.text

def Storage():
    print(datetime.datetime.now().strftime('%m-%d %H:%M'))
    print(getshuju())


def main():
    login()
    Storage()


if __name__ == '__main__':
    main()
#
# dictCookies = browser.get_cookies()
# jsonCookies = json.dumps(dictCookies)
# with open('cookies.json', 'w') as f:
#     f.write(jsonCookies)
# browser.get('https://mms.pinduoduo.com/Pdd.html#/directional/project?from=0')
# time.sleep(3)
# res = browser.find_element_by_css_selector('#direact_extension_project > table > tbody > tr:nth-child(2) > td:nth-child(6)')
# print(res.text)
# with open('cookies.json', 'r', encoding='utf-8') as f:
#     listCookies = json.loads(f.read())
# browser.get('https://mms.pinduoduo.com/Pdd.html#/index')
# browser.delete_all_cookies()
# for cookie in listCookies:
#     browser.add_cookie({
#         'domain': '.pinduoduo.com',  # 此处xxx.com前，需要带点
#         'name': cookie['name'],
#         'value': cookie['value'],
#         'path': '/',
#         'expires': None
#     })
# browser.get('https://mms.pinduoduo.com/Pdd.html#/index')
# browser.find_element_by_class_name("noFreightClose").click()
# browser.find_element_by_css_selector("#push-goods > div > div > div.react-modal-content > div.react-modal-footer > button.pdd-btn-gray.modal-btn").click()
# browser.find_element_by_css_selector("#left-nav-group7").click()
# browser.find_element_by_css_selector("#J_ManageSideNav > ul:nth-child(8) > li:nth-child(9) > a").click()
# time.sleep(2)
# browser.find_element_by_class_name("active").click()
#
#
# elem = browser.find_element_by_css_selector("#direact_extension_project > table > tbody > tr:nth-child(2) > td:nth-child(5) > div.search_plan_item > span.search_plan_txt.search_plan_number")
# print(elem.text)