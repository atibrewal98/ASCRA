#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 17:05:31 2022

@author: anirudhsfc
"""

import pandas as pd
import numpy as np
from Models.Common.sqlconnection import *

def getData(filename):
    df = pd.read_csv(filename)
    
    return df


#column namne sahi kro
#if all fields Nan toh delte the row


def getCountry(filename):
    
    df = getData(filename)
    df = df[["Country", "Code"]]
    df = df.drop_duplicates()
    df = df.rename( columns = {'Country' : 'country_name', 'Code' : 'country_code'})
    df = df.reset_index(drop = True)
    df = df[["country_name", "country_code"]]
    return df

def renamedf1(df):
   
    print(df.columns)
    df=df.rename(columns={'Country' : 'country_name', 'Code' : 'country_code', 'Year':'year','ContinentCode' : 'continent_code',
                          'Economic growth: the rate of change of real GDP' : 'gdp_growth_rate',
                          'Gross Domestic Product billions of U.S. dollars' : 'gdp', #in billions USD
                          'GDP per capita current U.S. dollars' : 'gdp_per_capita', #per person GDP
                          'Capital investment billion USD' : 'capital_investment', #in billions USD
                          'Household consumption billion USD' : 'household_consumption' ,#in billions USD
                          'Inflation: percent change in the Consumer Price Index' : 'inflation',
                          'Exports of goods and services billion USD' : 'exports',#in billions USD
                          'Imports of goods and services billion USD' : 'imports',#in billions USD
                          'Foreign Direct Investment billion USD' : 'foreign_investments',#in billions USD
                          'Net portfolio equity inflows' : 'net_equity_inflow',
                          'Current account balance billion USD' : 'current_account_balance',#in billions USD
                          'Trade balance billion USD': 'trade_balance',#in billions USD
                          'Foreign exchange reserves including gold billion USD' : 'foreign_exchange_reserves',#in billions USD
                          'Remittances million USD' : 'remittance', #IN MILLION USD NEED TO CONVERT
                          'Balance of payments net errors and omissions' : 'net_payment_error_balance',
                          'External debt percent of Gross National Income' : 'debt_percent_of_gni',
                          'Short-term debt percent of total external debt' : 'short_term_debt_percent',
                          'Short-term external debt percent of international reserves' : 'short_term_external_debt_percent',
                          'Government spending billion USD' : 'gov_spend', #billion usd
                          'Government debt as percent of GDP' : 'gov_debt', #as percent of gdp 
                          'Tax revenue percent of GDP' : 'tax_revenue', #percent of gdp
                          'Tax rate percent of commercial profits' : 'tax_rate_commercial',
                          'Taxes on goods and services percent of total revenue' : 'tax_of_total_revenue',
                          'Taxes on international trade percent of total revenue' : 'tax_trade_of_total_revenue',
                          'Income profits and capital gains taxes: percent of revenue' : 'tax_income_of_total_revenue',
                          'Foreign aid and official development assistance received' : 'foreign_aid_assistance',
                          'Economic growth forecast' : 'economic_growth_forecast',
                          'Investment forecast' : 'investment_forecast',
                          'Inflation forecast' : 'inflation_forecast',
                          'Liquid liabilities percent of GDP' : 'liability_liquid', #percent of gdp
                          'Bank assets percent of GDP' : 'assets_bank', #percent of gdp
                          'Bank credit to government and public enterprises percent of GDP':'credit_bank_to_gov', #%of gdp
                          'Stock market capitalization billion USD': 'stock_market_capital', #billions usd
                          'Stock market turnover ratio': 'stock_market_turnover', #ratio
                          'Stock market return percent' : 'stock_market_return',
                          'Mutual fund assets percent of GDP' : 'assets_mutual_fund', #percent of gdp
                          'Pension fund assets as percent of GDP' : 'assets_pension_fund', #%of gdp
                          'Population size in millions' : 'population', #millions
                          'Population growth percent' : 'population_growth',
                          'Health spending per capita' : 'health_spending',
                          'Life expectancy in years' : 'life_expectancy',
                          'Public spending on education percent of GDP' : 'public_spending_education', #%of gdp
                          'Literacy rate' : 'literacy_rate',
                          'Globalization index (0-100)': 'globalization_index',
                          'Economic globalization index (0-100)' : 'economic_gi',
                          'Political globalization index (0-100)' : 'political_gi',
                          'Social globalization index (0-100)' : 'social_gi',
                          'Energy use per capita' : 'energy',
                          'Income from natural resources percent of GDP' : 'income_natural_resources', #%of gdp
                          'Access to electricity percent of the population' : 'electricity_access', #of popuilation
                          'Renewable power generation billion kilowatthours': 'renewable_pg',
                          'Fossil fuels electricity generation billion kilowatthours' : 'fossil_pg',
                          'Wind electricity generation billion kilowatthours' : 'wind_pg',
                          'Solar electricity generation billion kilowatthours' : 'solar_pg',
                          'Hydroelectricity generation billion kilowatthours' : 'hydro_pg',
                          'Nuclear power generation billion kilowatthours' : 'nuclear_pg',
                          'Geothermal electricity generation billion kilowatthours' : 'geo_pg', #all power generationm in kilowatt hours
                          'Labor force million people': 'labour_force',
                          'Unemployment rate': 'unemplyment_rate',
                          'Youth unemployment ages 15-24' : 'youth_unemployment',
                          'Labor freedom index (0-100)' : 'labor_freedom_index',
                          'Human rights and rule of law index 0 (high) - 10 (low)' : 'rights_and_law_index',
                          'Month' : 'month',
                          'Long-term government bond yield' : 'yield',
                          'Agency' : 'agency',
                          'Rating' : 'rating',
                          'Outlook' : 'outlook'
                          })
    
    if 'remittance' in df.columns:
        
        df['remittance']=df['remittance']/1000000
    #converting million to billions
    df.iloc[ : , 5: ].dropna(how='all') 
    return df
    
    
def getNaAnalysis(df):
    lst=[]
    country = df['year'].unique()
    for c in country:
        df_fil = df.loc[df['year'] == c]
        NullCount = []
        for col in df_fil.columns:
            n = df_fil[col].isna().sum()
            NullCount.append(n/len(df_fil))
        
        missing = sum (NullCount)/len(NullCount)
        if(missing > 0.5):
            lst.append({c, missing})
    print(lst)
    
def getColNaAnalysis(df_fil):
    lst=[]
    for col in df_fil.columns:
        n = df_fil[col].isna().sum()
        
        missing = n/len(df_fil)
        if(missing > 0.3 ):
            lst.append({col, missing})
    print(lst)
  
    
    
    
    
def doEDA(df):
    
    df_country = getResult(" SELECT * from [country]")
    
    dic={}

    l = df_country.to_dict()

    for key in l['country_code']:
        dic[l['country_code'][key]] = l['country_id'][key] 
    
    df['country_id'] = -1
    # print(df['country_id'])
    for index, row in df.iterrows():
    
        df.at[index, 'country_id'] = dic[row['country_code']] 
#drop column names
    
    # print(df['country_id'])
    
    columns = df.columns[3:]
   
    
    
    # na values
    # getNaAnalysis(df)
    
    
    
    return df
        
    
def combineData(df1, df2, df3, dfEnv, dfGov, dfRating, dfYield):
    new_df = pd.merge(df1, df2,  how='left', left_on=['country_id','year'], right_on = ['country_id','year'])
    new_df = pd.merge(new_df, df3,  how='left', left_on=['country_id','year'], right_on = ['country_id','year'])
    new_df = pd.merge(new_df, dfEnv,  how='left', left_on=['country_id','year'], right_on = ['country_id','year'])
    new_df = pd.merge(new_df, dfGov,  how='left', left_on=['country_id','year'], right_on = ['country_id','year'])
    # new_df = pd.merge(new_df, dfSoc,  how='left', left_on=['country_id','year'], right_on = ['country_id','year'])
    new_df = pd.merge(new_df, dfRating,  how='left', left_on=['country_id','year'], right_on = ['country_id','year'])
    new_df = pd.merge(new_df, dfYield,  how='left', left_on=['country_id','year'], right_on = ['country_id','year'])

    return new_df

def compressData(df):
    dfRatingFinal = pd.DataFrame(columns = ['year','agency','rating','country_id','s&p','moodys','fitch'])
    
    # columns = df.columns[1:]
    # df = df[columns]
    if "continent_code" in df:
        df.drop("continent_code", axis=1, inplace=True)
    if "country_code" in df:
        df.drop("country_code", axis=1, inplace=True)
    if "country_name" in df:
        df.drop("country_name", axis=1, inplace=True)
    if "outlook" in df:
        df.drop("outlook", axis=1, inplace=True)
    
    
    if "month" in df:
        df.drop(df.index[df['month'] != 12], inplace=True)
        df.drop("month", axis=1, inplace=True) 
    if "agency" in df:
        df["s&p"] = ""
        df["moodys"] = ""
        df["fitch"] = ""
        
        for index, row in df.iterrows():
            
            if row['agency'] == 'Fitch':
                df.at[index,'fitch'] = row['rating']
        
            if row['agency'] == 'S&P':
                df.at[index,'s&p'] = row['rating']
            if row['agency'] == "Moody's":
                df.at[index,'moodys'] = row['rating']
        
        # df.drop("outlook", axis=1, inplace=True)
        
        for index, row in df.iterrows():
            
            
            # if 7 in list(dfRatingFinal['country_id'].values) and 2001 in list(dfRatingFinal['year'].values):
            #     print("sciosdjuosduiosdiosdhjadsihioj")
            df_temp = dfRatingFinal.loc[(dfRatingFinal['country_id'] == row['country_id']) & (dfRatingFinal['year'] == row['year'])]
            # print(df_temp.shape)
            
            if df_temp.shape[0] > 0:
                # print("helolooo")
                # print(df_temp)
                ind = df_temp.index[0]
                if row['s&p'] != "":
                    dfRatingFinal.at[ind,'s&p'] = row['s&p']
                if row['moodys'] != "":
                    dfRatingFinal.at[ind,'moodys'] = row['moodys']
                if row['fitch'] != "":
                    dfRatingFinal.at[ind,'fitch'] = row['fitch']
            else:
                dfRatingFinal = dfRatingFinal.append(row)
                # print("achaaa")
                
        return dfRatingFinal
    else:
        return df
            
    
    
    
def compressData1(df):
    
    columns = df.columns[3:]
   
    df = df[columns]
    
    return df

def fillData(df):
    if "agency" in df:
        df.drop("agency", axis=1, inplace=True)
    if "rating" in df:
        df.drop("rating", axis=1, inplace=True)
   
    mux = pd.MultiIndex.from_product([
        df.country_id.unique(),
        range(df.year.min(), df.year.max() + 1)
    ], names=['country_id', 'year'])

    df = df.set_index(['country_id', 'year']).reindex(mux).reset_index()
    df.fillna(method = 'ffill', inplace=True)
    df.fillna(method='bfill',inplace=True)
    df.replace(r'^\s*$', np.nan, regex=True,inplace= True)
    df.fillna(method='bfill',inplace=True)
    df.fillna(method = 'ffill', inplace=True)
    return df 
        
def getCleanData(filename):
    
    df = getData(filename)
    df = renamedf1(df)
    df = doEDA(df)
    if "BondYield.csv" in filename or "CreditRating.csv" in filename:
        df = compressData(df)
        
    else:
        df = compressData1(df)
    
    if "CreditRating.csv" in filename:
        df = fillData(df)
    return df


    
 
    