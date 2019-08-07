# citationOverTime
Get the number of citations of a paper over time

## requirements
- Chrome
- [chromedriver](http://chromedriver.storage.googleapis.com/index.html?path=77.0.3865.10/)
- pip install selenium webdriver_manager

## run
- set your user data path of chrom to prevent robot detecting of google
  - ie. `userProfile = r"C:\Users\yourName\AppData\Local\Google\Chrome\User Data\Default"`
- search paper (eg, `Policy gradient methods for reinforcement learning with function approximation`) by Google Scholar
- click `Cited by 2230` and get paper ID from the new url 
  - ie. `https://scholar.google.com/scholar?cites=14537753363344344488&as_sdt=2005&sciodt=0,5&hl=en`
  - `14537753363344344488` is the `paperID`
- set the `paperID` in `run.py`
- you can also set the time range (`startYear`, `endYear`, `interval`)
- `python run.py`
  - you will get the following result if using default setting
    ```
    DevTools listening on ws://127.0.0.1:59856/devtools/browser/d6614e5a-1a46-4245-b9ff-4ba91b8956e3
    1999 - 2 results (0.01 sec)
    2000 - 11 results (0.02 sec)
    2001 - About 28 results (0.03 sec)
    2002 - About 33 results (0.02 sec)
    2003 - About 36 results (0.03 sec)
    2004 - About 46 results (0.04 sec)
    ...
    ```
   
   - Maybe you will meet Error:
      ```
      [0807/140244.149:ERROR:cache_util_win.cc(21)] Unable to move the cache: Access is denied. (0x5)
      [0807/140244.150:ERROR:cache_util.cc(141)] Unable to move cache folder C:\Users\***\AppData\Local\Google\Chrome\User Data\Default\Default\Cache to C:\Users\***\AppData\Local\Google\Chrome\User Data\Default\Default\old_Cache_000
      [0807/140244.151:ERROR:disk_cache.cc(178)] Unable to create cache
      ```
      - Pls close all chrom pages and try again
    
    - Maybe you will get none caused by robot test of google
      ```
      DevTools listening on ws://127.0.0.1:59814/devtools/browser/135af13e-23fa-4972-9e68-af0507766c6e
      1999 -
      2000 -
      2001 -
      ...
      ```
       - Pls open '127.0.0.1:59814/devtools/browser/135af13e-23fa-4972-9e68-af0507766c6e' in chrom and complete the robot test
       - I promise you will not need to do this test in a short time (Once I know the length of the period, I will update it)
  
 ## Todo
 - Put setting into defults.py
 - Auto-get paperId by paper name 
 - Set default of startYear to the year when paper published
 - Set default of endYear to current year
 - Extract number of citation
 - Save numbers in scv and plot figure 
  ---
 - Hope you enjoy it :)
