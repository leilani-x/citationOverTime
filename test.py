from utils import *

## Paper setting ##################################################################
keyword = "deep+active+learning"  # TODO auto-get by paper name 
paperID = 14537753363344344488  # TODO auto-get by paper name
# please get it from google scholar

startYear = 1999                # TODO set default to the year when paper published
endYear = 2019                  # TODO set default to current year
interval = 1 

chromedriverPath = r"/Users/lei/Downloads/chromedriver"
###################################################################################

# getData(chromedriverPath, keyword, startYear, endYear, interval, mode='keyword')
getData(chromedriverPath, paperID, startYear, endYear, interval, mode='paperID')
