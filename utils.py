from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time, os
import matplotlib.pyplot as plt
import pickle 

def plotLine(x,y,title):
    plt.figure(figsize=(18, 6))
    plt.title(title)    
    plt.ylabel("number")
    plt.xlabel("years") 
    plt.plot(list(map(str,x)), y)       
    plt.show()          

def getData(chromedriverPath, msg, startYear, endYear, interval, mode='keyword'):
    # set webdriver
    chrome_options = webdriver.ChromeOptions()
    userProfile = r"./"
    chrome_options.add_argument('--headless')
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    # chrome_options.add_argument("user-data-dir={}".format(userProfile))
    
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriverPath)
    # joint url 
    if mode == 'keyword':
        basicUrl = "https://scholar.google.com/scholar?hl=en&as_sdt=1%2C5&as_ylo={}"+ "&as_vis=1&q=" + str(msg)  + "&btnG="
    elif mode == 'paperID':
        basicUrl = 'https://scholar.google.com/scholar?hl=en&as_sdt=2005&sciodt=0%2C5&cites='+ str(msg) + '&scipsc=&as_ylo={}'
    else:
        print('no such mode :)')
        return
    
    # import pdb; pdb.set_trace()
    # get data
    nums = []
    for i in range(startYear, endYear+1, interval):
        finalUrl = basicUrl.format(str(i) + '&as_yhi=' + str(i+interval-1))
        driver.get(finalUrl)
        element = driver.find_element_by_id('gs_ab_md')
        data = element.text
        if data.split()[0] != 'About':
            number = data.split()[0]
        else:
            number = data.split()[1]
        nums.append(int("".join(number.split(','))))
        print('year: {}, about {} results'.format(i, number)) 
        time.sleep(2)
    
    # plot figure
    plotLine(list(range(startYear, endYear+1)), nums, msg)

