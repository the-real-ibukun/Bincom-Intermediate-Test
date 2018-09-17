"""7.	Extract male and female friends of different Facebook users and build a table to hold
 them for data analysis . 
Build a classification model that will tell the gender of a
 Facebook user given the amount of male and female friends he has.
"""
    
from selenium import webdriver
import mechanicalsoup
import json
import time
import requests
import re
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

chrome = webdriver.Chrome()

browser = mechanicalsoup.StatefulBrower()

f = csv.writer(open('q7.csv', 'w'))
f.writerow(['Name','Gender', 'Male_no', 'Female_no'])


def save_jsn(jsn,file):
    with open(file, 'w') as f:
        json.dump(jsn,f)

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
    
def mech():
    chrome.get('http://www.facebook.com/login')
    use_cookies()
    chrome.get('http://www.facebook.com/login')

    chrome.get('https://www.facebook.com/search/males/me/friends/intersect')
    time.sleep(30)    
    p = chrome.find_elements_by_xpath('//*[@class="_32mo"]')

    chrome.get('https://web.facebook.com/search/me/friends/females/intersect')
    time.sleep(30) 
    p1 = chrome.find_elements_by_xpath('//*[@class="_32mo"]')

    chrome.get('https://web.facebook.com/ibukun.agboola.1/about?section=contact-info')
    p2 = chrome.find_elements_by_xpath('//*[@id="pagelet_basic"]/div/ul/li[3]/div/div[2]/div/div')
    p3 = chrome.find_elements_by_xpath('//*[@class="_2nlw _2nlv"]')    

    #print(len(p),len(p1),p2[0].text,p3)

    for n,g,m,f in zip(p3,p2[0].text,len(p),len(p1)):
        f.writerow(n,g,m,f)

    mfriend = [i.lower().split(' ').join('.') for i in p]
    for j in friend:
        browser.open('https://web.facebook.com/'+ j +'/about?section=contact-info')
        p4 = chrome.find_elements_by_xpath('//*[@id="pagelet_basic"]/div/ul/li[3]/div/div[2]/div/div')
        p5 = chrome.find_elements_by_xpath('//*[@class="_2nlw _2nlv"]')

        chrome.get('https://www.facebook.com/search/males/'+ j +'/friends/intersect')
         time.sleep(30)    
        p6 = chrome.find_elements_by_xpath('//*[@class="_32mo"]')

        chrome.get('https://web.facebook.com/search/'+ j +'/friends/females/intersect')
        time.sleep(30) 
        p7 = chrome.find_elements_by_xpath('//*[@class="_32mo"]')

        for n1,g1,m1,f1 in zip(p4,p5[0].text,len(p6),len(p7)):
            f.writerow(n1,g1,m1,f1)

    ffriend = [i.lower().split(' ').join('.') for i in p1]
    for k in ffriend:
        browser.open('https://web.facebook.com/'+ k +'/about?section=contact-info')
        p8 = chrome.find_elements_by_xpath('//*[@id="pagelet_basic"]/div/ul/li[3]/div/div[2]/div/div')
        p9 = chrome.find_elements_by_xpath('//*[@class="_2nlw _2nlv"]')

        chrome.get('https://www.facebook.com/search/males/'+ k +'/friends/intersect')
         time.sleep(30)    
        p0 = chrome.find_elements_by_xpath('//*[@class="_32mo"]')

        chrome.get('https://web.facebook.com/search/'+ k +'/friends/females/intersect')
        time.sleep(30) 
        p01 = chrome.find_elements_by_xpath('//*[@class="_32mo"]')

        for n2,g2,m2,f2 in zip(p8,p9[0].text,len(p0),len(p01)):
            f.writerow(n2,g2,m2,f2)

    



mech()
def get_gen():
    
    dataset = pd.read_csv('q7.csv')
    X = dataset.iloc[:,2:].values
    y = dataset.iloc[:,1].values


    
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    

    y_pred = classifier.predict(X_test)

    
