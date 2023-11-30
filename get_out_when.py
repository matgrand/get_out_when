# script to open the brower, navigate through some websites, and get the last entry of a table

#lets use selenium to open the browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#lets use pandas to read the table
import pandas as pd

#lets use time to wait for the page to load
import time

#lets use os to get the path of the file
import os

SLEEP = 1 #seconds

FIRST_URL = 'https://mail.dei.unipd.it/horde5/imp/dynamic.php?page=mailbox#mbox:SU5CT1g'

#open the browser
browser = webdriver.Chrome()
browser.get(FIRST_URL)

#wait for the page to load
time.sleep(SLEEP)

#show the page
browser.maximize_window()

#close the browser
browser.close()
