# -*- coding: utf-8 -*-


from Models.Database import clean as clean
from Models.Database import imputeData
from Models.Common.sqlconnection import insertData, getResult

def cleanAndInsertData():
    df = clean.getCountry('./dataset/data/1.csv')
    insertData(df, 'country')
    
    df1 = clean.getCleanData('./dataset/data/1.csv')
    df2 = clean.getCleanData('./dataset/data/2.csv')
    df3 = clean.getCleanData('./dataset/data/3.csv')
    dfEnv = clean.getCleanData('./dataset/data/Env.csv')
    dfGov = clean.getCleanData('./dataset/data/Gov.csv')
    dfBond = clean.getCleanData('./dataset/data/BondYield.csv')
    dfRating = clean.getCleanData('./dataset/data/CreditRating.csv')
    insertData(df1, 'temp1')
    insertData(df2, 'temp2')
    insertData(df3, 'temp3')
    insertData(dfEnv, 'tempEnv')
    insertData(dfGov, 'tempGov')
    insertData(dfBond, 'tempYield')
    insertData(dfRating, 'tempRating2')

def doNA():
    df1 = getResult('Select * from temp1')
    df2 = getResult('Select * from temp2')
    df3 = getResult('Select * from temp3')
    dfEnv = getResult('Select * from tempEnv')
    dfGov = getResult('Select * from tempGov')
    dfRating = getResult('Select * from tempRating')
    dfYield = getResult('Select * from tempYield')
    dfFinal = clean.combineData(df1, df2, df3, dfEnv, dfGov, dfRating, dfYield)
    clean.getNaAnalysis(df1)
    clean.getNaAnalysis(df2)
    clean.getNaAnalysis(df3)
    clean.getNaAnalysis(dfEnv)
    clean.getNaAnalysis(dfGov)
    clean.getNaAnalysis(dfFinal)
    clean.getColNaAnalysis(dfFinal)

def doImputation():
    df1 = getResult('Select * from temp1')
    df2 = getResult('Select * from temp2')
    df3 = getResult('Select * from temp3')
    dfEnv = getResult('Select * from tempEnv')
    dfGov = getResult('Select * from tempGov')
    dfRating = getResult('Select [country_id], [year], [s&p] from rating')
    # dfRating = getResult('Select * from rating')
    dfYield = getResult('Select * from tempYield')
    dfFinal = clean.combineData(df3, df2, df1, dfEnv, dfGov, dfYield, dfRating)
    
    # imputeData.getImputorAnalysis(dfFinal)
    
    clean.getColNa(dfFinal)
    

# doImputation()
    