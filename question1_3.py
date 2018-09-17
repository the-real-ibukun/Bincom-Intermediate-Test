'''
1.	Write a script that crawls posts of your Facebook friends.
3.	In order to avoid your Facebook account being locked, get the login cookies for your script.
'''
import json
import requests
import mechanicalsoup
import re
from selenium import webdriver


big_json = []
info = {}
chrome = webdriver.Chrome()

def save_jsn(jsn,file):
    with open(file, 'w') as f:
        json.dump(jsn,f)

def load_jsn(file):
    with open(file) as f:
       data = json.load(f)
    return data

def get_cookies():
    chrome = webdriver.Chrome()
    chrome.get('http://www.facebook.com/login')
    email = chrome.find_element_by_id('email')
    email.send_key('******') 

    pass1 = chrome.find_element_by_id('pass')
    pass1.send_key('******')
    pass1.submit()

    cookie = chrome.get_cookies()
    file = 'cookies.json'
    save_jsn(cookie,file)

def create_jsn(name,post):
    info['Name'] = name 
    info['Post'] = post

    big_json.append(info.copy())

def use_cookies():
    file = 'cookies.json'
    load_jsn(file)
     
    data = load_jsn(file)
    for i in data:
        chrome.add_cookie(i)
    
    

def scrap_post():

    chrome.get('http://www.facebook.com/login')
    use_cookies()
    chrome.get('http://www.facebook.com/login')

    chrome.get('https://www.facebook.com/search/100001560217395/friends/stories-by')
    

    p = chrome.find_elements_by_xpath('//*[@class="_vwp"]')
    p1 = chrome.find_elements_by_xpath('//*[@class="_5-jo"]')
    
    for i in range(len(p)-1):
        create_jsn(p[i].text,p1[i].text)
    
    print(len(p),len(p1))


    file = 'post.json'

    save_jsn(big_json,file)

scrap_post()