# Import the necessary modules for development

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
 
# Invoke a new Chrome Instance
ff_driver = webdriver.Chrome()
 
# Blocking wait of 30 seconds in order to locate the element
ff_driver.implicitly_wait(30)
ff_driver.maximize_window()
 
# Open the Home Page
ff_driver.get("https://www.topuniversities.com/university-rankings/world-university-rankings/2021")
 
# Look for the Search Element and enter the Search Criteria
 
search_criteria = ff_driver.find_element_by_link_text("More")
actionChains = ActionChains(ff_driver)
actionChains.context_click(search_criteria).perform()
time.sleep(5)
 
# Perform action on the Images Link
ActionChains(ff_driver) \
    .key_down(Keys.CONTROL) \
    .click(search_criteria) \
    .key_up(Keys.CONTROL) \
    .perform()
    
 
# Sleep for 10 seconds in order to see the results
time.sleep(10)
 
results =  ff_driver.find_elements_by_class_name('criteria')

for quote in results:
    quoteArr = quote.text.split('\n')
    print(quoteArr)
    print()

# Close the Browser instance
ff_driver.close()
