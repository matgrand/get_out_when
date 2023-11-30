
# script to open the brower, navigate through some websites, and get the last entry of a table

#lets use selenium to open the browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#lets use pandas to read the table
import pandas as pd

#lets use time to wait for the page to load
from time import time, sleep
#lets use os to get the path of the file
import os

SLEEP = 1 #seconds

FIRST_URL = 'https://mail.dei.unipd.it/horde5/imp/dynamic.php?page=mailbox#mbox:SU5CT1g'

#open the browser
browser = webdriver.Chrome()
browser.get(FIRST_URL)

sleep(SLEEP) #wait for the page to load

#login 
from credentials import USER_NAME, USER_PASSWORD

def print_all_elements():
    #print all element ids
    all_elements = browser.find_elements(By.XPATH, '//*')
    print(f'All elements: {len(all_elements)}')
    for element in all_elements:
        print(element.get_attribute('id'))


#print all element ids
print_all_elements()




#find the username field
username = browser.find_element(By.ID, 'horde_user')
#fill the username field
username.send_keys(USER_NAME)

#find the password field
password = browser.find_element(By.ID, 'horde_pass')
#fill the password field
password.send_keys(USER_PASSWORD)

#press enter
password.send_keys(Keys.RETURN)







print('Page loaded, sleeping for 5 seconds')
sleep(5)


print_all_elements()

#close the browser
browser.close()


