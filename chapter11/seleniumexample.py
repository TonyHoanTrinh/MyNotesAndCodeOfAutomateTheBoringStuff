#! /usr/bin/env python3
'''
There is a lot of different methods with selenium and you will have to
look up documentation to be able to web scrape and manipulate the browser
'''
from selenium import webdriver

browser = webdriver.Firefox(executable_path='./geckodriver.exe')
print(type(browser))
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with name')
