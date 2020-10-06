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
 
# Invoke a new Chrome Instance
ff_driver = webdriver.Chrome()
 
# Blocking wait of 30 seconds in order to locate the element
ff_driver.implicitly_wait(30)
ff_driver.maximize_window()
 
# Open the Home Page
ff_driver.get("https://www.topuniversities.com/university-rankings/world-university-rankings/2021")

for i in range(1, 26):

    buttons = ff_driver.find_elements_by_css_selector(f"#qs-rankings > tbody > tr:nth-child({i}) > td.uni > div > a.more")
    
#    print(buttons)

    for j in range(len(buttons)):
    
        ff_driver.execute_script("arguments[0].click();", buttons[j])
        
        ff_driver.implicitly_wait(10)
        
        results =  ff_driver.find_elements_by_class_name('criteria')
            
        name = []
        key = []
        value = []
            
        header = ff_driver.find_element_by_class_name('title')
        
        for quote in results:
            quoteArr = quote.text.split('\n')
            for line in quoteArr:
                if line is not None:
                    key.append(str(line).split(':')[0])
                    value.append(str(line).split(':')[1])
                    name.append(header)
                else:
                    key.append('')
                    value.append('')
                    name.append(header)
                    
                    data = {'name':name, 'key': key, 'value': value}
                
                    df = pd.DataFrame(data)
               
                    df.to_csv('test_output_new_3.csv', index = False)
            
                print(quoteArr)
                print()
                
                with open(r'test_output_new_3.csv', 'a', newline='') as csvfile:
                    fieldnames = ['name','key', 'value']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'name':name, 'key':key, 'value': value})
           
        ff_driver.implicitly_wait(10)
            
        ff_driver.execute_script("window.history.go(-1)")
        
        ff_driver.implicitly_wait(5)
        
ff_driver.close()
