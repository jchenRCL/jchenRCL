# Import the necessary modules for development

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys
import pandas as pd
import csv
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as UI
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# need the below imports to work with Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Invoke a new Chrome Instance
ff_driver = webdriver.Chrome()
 
# Blocking wait of 30 seconds in order to locate the element
ff_driver.implicitly_wait(30)
ff_driver.maximize_window()
 
# Open the Home Page
ff_driver.get("https://www.topuniversities.com/university-rankings/world-university-rankings/2021")

# the first 25 records in the first page

for i in range(1, 25):

    buttons = ff_driver.find_elements_by_css_selector(f"#qs-rankings > tbody > tr:nth-child({i}) > td.uni > div > a.more")
    
#   print(buttons)

    for j in range(len(buttons)):
    
        ff_driver.execute_script("arguments[0].click();", buttons[j])
        
        ff_driver.implicitly_wait(10)
        
        results =  ff_driver.find_elements_by_class_name('criteria')
        
        # print the Ranking Criteria in the terminal 

        for quote in results:
            quoteArr = quote.text.split('\n')
            print(quoteArr)
            print()
            
        ff_driver.implicitly_wait(10)
            
        ff_driver.execute_script("window.history.go(-1)")
            
ff_driver.close()




    
