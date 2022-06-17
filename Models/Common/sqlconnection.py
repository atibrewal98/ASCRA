#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:29:15 2022

@author: anirudhsfc
"""
import pypyodbc
from Models.Common import config as config
# import config as config
def getConnection():
    sql = config.SQL_CONFIG
    
    connection = pypyodbc.connect("Driver={" + sql["Driver"]+"};Port=" + str(sql['Port']) + ";Server=" + sql["Server"] + ";Database=" + sql["Database"] + ";uid=" + sql["UID"] + ";pwd=" + sql["Password"], autocommit=True)

    return connection

# connection=getConnection()

# connection.close()
