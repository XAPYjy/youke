#!/usr/bin/python3
# coding: utf-8

from selenium.webdriver import Chrome
import time

import xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

base_url = 'http://47.92.132.161:9001'

login_url = base_url+'/back/login/'
user_name = 'admin'
password = 'admin'

driver = 'chromedriver'

chrome = Chrome(driver)
chrome.get(login_url)

time.sleep(2)
# 填充用户名和口令
chrome.find_element_by_id('username').send_keys(user_name)
time.sleep(1)
chrome.find_element_by_id('password').send_keys(password)
time.sleep(1)

# 发起点击登录按钮
chrome.find_element_by_id('login').click()
time.sleep(2)

print(chrome.current_url)
if chrome.current_url != login_url:
    print('---登录成功--')

    # 请求用户角色列表
    chrome.get(base_url+'/back/role/')
    time.sleep(1.5)
    # 添加用户角色
    chrome.find_element_by_id('add_role').click()
    time.sleep(2)
    chrome.find_element_by_id('add1_name').send_keys('管理员')
    time.sleep(2)
    chrome.find_element_by_id('add1_code').send_keys('disen')
    time.sleep(2)
    chrome.find_element_by_id('add_role_sure').click()
    time.sleep(2)

    # 编辑用户角色
    chrome.find_element(By.ID, 'table_role').find_elements(By.TAG_NAME, "tr")[-1].find_elements(By.TAG_NAME,'td')[-1].find_element(By.ID,'edit1_role').click()
    time.sleep(2)
    chrome.find_element(By.ID, 'edit_name').send_keys('1')
    time.sleep(2)
    chrome.find_element(By.ID,'edit_sure').click()
    time.sleep(2)

    # 删除用户角色
    # chrome.find_element(By.ID, 'table_role').find_elements(By.TAG_NAME, "tr")[-1].find_elements(By.TAG_NAME, 'td')[-1].find_element(By.ID, 'del_role').click()
    # time.sleep(1)
    # chrome.find_element(By.ID,'delete_sure').click()
    # time.sleep(1)

    chrome.get(base_url + '/back/uuser/')
    time.sleep(2)
    chrome.find_element(By.ID, 'table_user').find_elements(By.TAG_NAME, "tr")[-1].find_elements(By.TAG_NAME, 'td')[-1].find_element(By.ID, 'del_user').click()
    time.sleep(2)
    chrome.refresh()
    time.sleep(3)
    chrome.get(base_url + '/back/uorder/')
    time.sleep(2)
    chrome.get(base_url + '/back/lfirst/')
    time.sleep(3)
    chrome.get(base_url + '/back/lsecond/')
    time.sleep(3)
    chrome.get(base_url + '/back/lmessage/')
    time.sleep(2)
    chrome.execute_script("document.documentElement.scrollTop=15000")
    time.sleep(2)
    chrome.find_element(By.ID, 'bt_next').click()
    time.sleep(2)
    chrome.execute_script("document.documentElement.scrollTop=15000")
    time.sleep(2)
    chrome.find_element(By.ID, 'table_lesson').find_elements(By.TAG_NAME, "tr")[-1].find_elements(By.TAG_NAME, 'td')[1].find_element(By.ID,'a_video').click()
    time.sleep(4)
    # chrome.find_element_by_xpath("//button[@class='vjs-big-play-button']/span[@class='vjs-icon-placeholder']").click()
    # time.sleep(5)
    chrome.get(base_url + '/back/torder/')
    time.sleep(3)
    chrome.get(base_url + '/back/tuser/')
    time.sleep(3)
    chrome.get(base_url + '/back/tlesson/')
    time.sleep(3)
    chrome.get(base_url + '/back/')
    time.sleep(2)
    chrome.find_element(By.ID,'top_aa' ).click()
    time.sleep(2)
    chrome.find_element(By.ID,'top_aa' ).find_element(By.ID, 'top_init').click()
    time.sleep(2)
    chrome.find_element(By.ID, 'top_aa').click()
    time.sleep(2)
    chrome.find_element(By.ID, 'top_aa').find_element(By.ID, 'log_out').click()
    time.sleep(2)
else:
    print('---登录失败--')


