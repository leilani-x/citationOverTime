from utils import setWebDriver, getPaperByKeys
from searchSet import SearchSet

class PaperByKeywords(SearchSet):
    def __init__(self, keywordList, chromedriverPath, startYear, endYear, yearStep=1, viewChrome=False):
        keyWordInUrl = ''
        for keyword in keywordList:
            keyword.replace(' ', '+')
            keyWordInUrl += '+AND+%22{}%22'.format(keyword)
        self.msg = keyWordInUrl
        print('******************* KeyWords: ', keyWordInUrl)
        super(PaperByKeywords, self).__init__(chromedriverPath, startYear, endYear, yearStep, viewChrome)
        self.papers = getPaperByKeys(self.years, self.basicUrl, self.driver)
        self.quitWebDriver()

    def concateURL(self):
        return "https://scholar.google.com/scholar?as_vis=1&start={}&hl=en&as_sdt=1%2C5&as_ylo={}&q=" + str(self.msg) + "+&btnG="

