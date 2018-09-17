'''
2.	Write a script that crawls the groups joined by your Facebook friends
'''

import json
import requests
import mechanicalsoup
import re
from selenium import webdriver
s = requests.Session()

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

def create_jsn(name,members):

    info['Group Name'] = name 
    info['Members'] = members
    big_json.append(info.copy())


def use_cookies():
    file = 'cookies.json'
    load_jsn(file)
     
    data = load_jsn(file)
    for i in data:
        chrome.add_cookie(i)
    

def scrap_groups():
    chrome.get('http://www.facebook.com/login')
    use_cookies()
    chrome.get('http://www.facebook.com/login')
 
    chrome.get('https://www.facebook.com/search/100001560217395/friends/groups')


    p = chrome.find_elements_by_xpath('//*[@*]/div/div[2]/div/div[1]/div[2]/div/div/a')
    p1 = chrome.find_elements_by_xpath('//*[@class="_pac"]')
    for i in range(len(p)):
        create_jsn(p[i].text,p1[i].text)
        
    
    
    file = 'groups.json'

    save_jsn(big_json,file)

scrap_groups()