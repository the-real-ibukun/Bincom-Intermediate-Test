'''
5.	If we have a confidence level of 0-100 on a Facebook user depending on the favorite pages, 
the groups they join, the number of female friends they have, the number of mutual friends they have, 
build a regression model that will tell us the confidence level of any Facebook user given all these parameters.
'''

import json
import requests
import mechanicalsoup
import re
import time
from selenium import webdriver
import numpy as np
import scipy.stats


chrome = webdriver.Chrome()

def save_jsn(jsn,file):
    with open(file, 'w') as f:
        json.dump(f,jsn)

def load_jsn(file):
    with open(file) as f:
       data = json.load(f)
    return data

def use_cookies():
    file = 'cookies.json'
    load_jsn(file)
     
    data = load_jsn(file)
    for i in data:
        chrome.add_cookie(i)

def mutual():
    chrome.get('http://www.facebook.com/login')
    use_cookies()
    chrome.get('http://www.facebook.com/login')

    chrome.get('https://www.facebook.com/search/me/friends/100001560217395/friends/intersect')
    time.sleep(30)
   

    p = chrome.find_elements_by_xpath('//*[@*]/div/div[1]/div/div/div')
    
    
    mutl = len(p)
    return mutl

    
    
def fem_frd():
    
    chrome.get('https://www.facebook.com/search/100001560217395/friends/intersect/females/intersect')
    

    p = chrome.find_elements_by_xpath('//*[@class="_32mo"]')
    
    fem = len(p)
    return fem

def groups():
    file = 'groups.json'
    load_jsn(file)
    data = load_jsn(file)
    return data

grp = groups()
fm = fem_frd()
mt = mutual()

data = (grp,fm,mt)


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

