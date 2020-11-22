from numByYears import KeywordPaperNumByYears, PaperCitedsNumByYears

### 1. webDriver Setting ##########################################
viewChrome = False
chromedriverPath = r"/Users/lei/Downloads/chromedriver"

### 2. Task Setting ##############################################
####### 2.1 put the keyword which you want to analysis;
keywords = ["deep+reinforcement+learning"] 

####### 2.2 put the id of the paper which you want to analysis;
paperIDs = [14537753363344344488 ]
########### you can get the paper id from google scholar;

####### 2.3 set the x_axis, and you can set more than one x_axis;
startYears = [1999]            
endYears = [2020]  
yearSteps = [1]

####### 2.4 show or save data
showImg = False

saveImg = True
saveImgPath="./saveData/images/"

saveNums = True
saveNumsPath = './saveData/numsCsv/'
###################################################################

if __name__ == '__main__':
    # get all data
    numByYears = []
    for startYear, endYear, yearStep in zip(startYears, endYears, yearSteps):
        for keyword in keywords:
            numByYears.append(KeywordPaperNumByYears(keyword, chromedriverPath, startYear, endYear, yearStep, viewChrome))

        for paperID in paperIDs:
            numByYears.append(PaperCitedsNumByYears(paperID, chromedriverPath, startYear, endYear, yearStep, viewChrome))

    # show and save all data
    for numByYear in numByYears:
        numByYear.plotNums()
        
        basicSaveFileName = '{}_{}_{}_{}'.format(numByYear.msg, str(startYear), str(endYear), str(yearStep))
        if showImg: numByYear.imgShow()
        if saveImg: numByYear.imgSave(saveImgPath, basicSaveFileName + '.png')
        if saveNums: numByYear.saveNums(saveNumsPath, basicSaveFileName + '.csv')
        numByYear.quitWebDriver()

