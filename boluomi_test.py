#coding:utf-8
from selenium import webdriver
driver = webdriver.Chrome()
import time
driver.get("https://www.baidu.com")
driver.quit()
prin("shanghai")