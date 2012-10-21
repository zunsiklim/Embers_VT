#-*- coding:utf8-*-

import WarningCreate
import RawNewsProcess
import RawStockProcess

def execute(predictionDate,rawStockFilePath,rawNewsFilePath):
    #process raw Stock Process data
    RawStockProcess.execute(rawStockFilePath)
    #process raw news data
    RawNewsProcess.execute(rawNewsFilePath)
    #Warning Create
    WarningCreate.execute(predictionDate)
    
    
if __name__ == "__main__":
    execute("2012-10-20",'../Test/stock_2012-10-01.txt','../Config/Data/DailyNews/Bloomberg-News-2012-10-20')