from utils import plotLine, imgShow, imgSave, getNumByYear, saveNums
from searchSet import SearchSet

class NumByYears(SearchSet):
    def __init__(self, chromedriverPath, startYear, endYear, yearStep=1, viewChrome=False):
        super(NumByYears, self).__init__(chromedriverPath, startYear, endYear, yearStep, viewChrome)
        self.nums = getNumByYear(self.years, self.basicUrl, self.driver)
        self.quitWebDriver()
        
    def plotNums(self, title=None):
        plotLine(self.years[:-1], self.nums, title)

    def imgShow():
        imgShow()

    def imgSave(self, savePath="./saveData/images/", saveFileName='img.png'):
        imgSave(savePath, saveFileName)

    def saveNums(self, savePath='./saveData/numsCsv/', saveFileName='num.csv'):
        saveNums(self.years[:-1], self.nums, savePath, saveFileName)

class KeywordPaperNumByYears(NumByYears):
    def __init__(self, keyword, chromedriverPath, startYear, endYear, yearStep=1, viewChrome=False):
        self.msg = keyword
        super(KeywordPaperNumByYears, self).__init__(chromedriverPath, startYear, endYear, yearStep, viewChrome)

    def concateURL(self):
        return "https://scholar.google.com/scholar?as_vis=1&hl=en&as_sdt=1%2C5&as_ylo={}&q=" + str(self.msg)  + "&btnG="

class PaperCitedsNumByYears(NumByYears):
    def __init__(self, paperID, chromedriverPath, startYear, endYear, yearStep=1, viewChrome=False):
        self.msg = paperID
        super(PaperCitedsNumByYears, self).__init__(chromedriverPath, startYear, endYear, yearStep, viewChrome)

    def concateURL(self):
        return 'https://scholar.google.com/scholar?as_vis=1&hl=en&as_sdt=2005&sciodt=0%2C5&cites='+ str(self.msg) + '&scipsc=&as_ylo={}'
