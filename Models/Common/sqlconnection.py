#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:29:15 2022

@author: anirudhsfc
"""
import pypyodbc
import urllib 
import sqlalchemy as sa
from Models.Common import config as config
import pandas as pd

def getConnection():
    sql = config.SQL_CONFIG
    
    connection = pypyodbc.connect("Driver={" + sql["Driver"]+"};Port=" + str(sql['Port']) + ";Server=" + sql["Server"] + ";Database=" + sql["Database"] + ";uid=" + sql["UID"] + ";pwd=" + sql["Password"], autocommit=True)

    return connection



def insertData(df, table_name, index = False ):
    
    df.to_sql(table_name, getSQLAlchemyConnection(), if_exists = 'append', index = index)




def getSQLAlchemyConnection():
    params = config.SQL_CONFIG

    p = 'DRIVER=' + params['Driver'] + ';' \
        'SERVER=' + params['Server'] + ';' \
        'DATABASE=' + params['Database'] + ';' \
        'UID=' + params['UID'] + ';' \
        'PWD=' + params['Password'] + ';' \
        'PORT=' + str(params['Port']) + ';'
            
    p = urllib.parse.quote_plus(p)
    db = sa.create_engine('mssql+pyodbc:///?odbc_connect=%s' % p)
    return db

def getResult(query):
    
    df = pd.read_sql_query(query, getConnection())
    return df