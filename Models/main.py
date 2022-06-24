# -*- coding: utf-8 -*-


from Models.Database import clean as clean
from Models.Common.sqlconnection import insertData 


# df = clean.getCountry('./dataset/data/1.csv')
# insertData(df, 'country')

df1 = clean.getCleanData('./dataset/data/1.csv')
df2 = clean.getCleanData('./dataset/data/2.csv')
df3 = clean.getCleanData('./dataset/data/3.csv')
dfEnv = clean.getCleanData('./dataset/data/Env.csv')
dfGov = clean.getCleanData('./dataset/data/Gov.csv')
dfSoc = clean.getCleanData('./dataset/data/Social.csv')
insertData(df1, 'temp1')
insertData(df2, 'temp2')
insertData(df3, 'temp3')
insertData(dfEnv, 'tempEnv')
insertData(dfGov, 'tempGov')
insertData(dfSoc, 'tempSoc')