from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time, os
from utils import *

###################################################################################
# Setting##########################################################################

## Paper setting ##################################################################

keyword = "deep+reinforcement+learning+DRL"  # TODO auto-get by paper name 
# please get in google scholar

startYear = 1999                # TODO set default to the year when paper published
endYear = 2019                  # TODO set default to current year
interval = 1 

## Basic setting ##################################################################
#userProfile = r"C:\Users\yourName\AppData\Local\Google\Chrome\User Data\Default"
chromedriverPath = r"/Users/lei/Downloads/chromedriver"
###################################################################################

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("start-maximized")
#chrome_options.add_argument("user-data-dir={}".format(userProfile))

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriverPath)
basicUrl = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&sciodt=0%2C5&cites='

print("==========keyword:",keyword)

nums = []
for i in range(startYear, endYear+1, interval):
    finalUrl = "https://scholar.google.com.hk/scholar?hl=en&as_sdt=1%2C5&as_ylo=" + str(i) + '&as_yhi=' + str(i+interval-1) + "&as_vis=1&q=" + str(keyword) + "&btnG="
    #print(finalUrl)
    driver.get(finalUrl)
    element = driver.find_element_by_id('gs_ab_md')
    driver.find_elements_by_class_name('gs_ab_mdw')
    data = element.text
    if data.split()[0] != 'About':
        number = data.split()[0]
    else:
        number = data.split()[1]
    nums.append(int("".join(number.split(','))))
    print('year: {}, about {} results'.format(i, number)) 
    time.sleep(2)

plotLine(list(range(startYear, endYear+1)), nums, keyword)
