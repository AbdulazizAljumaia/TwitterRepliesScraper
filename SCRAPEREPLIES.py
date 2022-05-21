import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

domain = 'PUT THE TWEETS LINK'


driver = webdriver.Chrome(executable_path='PATH_TO_THE_DRIVER')

driver.get(domain)
time.sleep(3)

SCROLL_PAUSE_TIME = 1.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    

Name = []
Account = []
Date = []
Content = []
count = []


for z in range(10):
    try:
        TruthofExistence = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div['+ str(z) +']').text
        if len(TruthofExistence.split('\n', 5)[0]) > 0 and TruthofExistence != 'Show replies':
            Name.append(TruthofExistence.split('\n', 5)[0])
        Account.append(TruthofExistence.split('\n', 5)[1])
        Date.append(TruthofExistence.split('\n', 5)[3])
        Content.append(TruthofExistence.split('\n', 5)[5])
        count.append(z)
        
        print(TruthofExistence)
    except:
        pass
    

