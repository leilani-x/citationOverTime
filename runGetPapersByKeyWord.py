from src.paperByKeywords import PaperByKeywords

### 1. webDriver Setting ##########################################
viewChrome = True
chromedriverPath = r"/Users/lei/Downloads/chromedriver"

### 2. Task Setting ##############################################
####### 2.1 put the keyword which you want to analysis;
keywords = [["The Conference on Robot Learning", "2020"]]

####### 2.2 set the x_axis, and you can set more than one x_axis;
startYears = [2019]         
endYears = [2019]  
yearSteps = [1]

####### 2.3 save data to txt / pdf

###################################################################
    
if __name__ == '__main__':
    # get all data
    papers = []
    for startYear, endYear, yearStep in zip(startYears, endYears, yearSteps):
        for keyword in keywords:
            papers.append(PaperByKeywords(keyword, chromedriverPath, startYear, endYear, yearStep, viewChrome))

    # show and save all data
    for paper in papers:
        paper.saveMarkdown()

