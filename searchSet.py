from utils import setWebDriver

class SearchSet():
    def __init__(self, chromedriverPath, startYear, endYear, yearStep=1, viewChrome=False):
        self.years = list(range(startYear, endYear + yearStep*2, yearStep))
        self.basicUrl = self.concateURL()
        self.driver = setWebDriver(chromedriverPath, viewChrome)

    def concateURL(self):
        raise NotImplementedError

    def quitWebDriver(self):
        self.driver.quit()