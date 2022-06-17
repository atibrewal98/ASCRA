#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 17:05:31 2022

@author: anirudhsfc
"""

import pandas as pd

def getData(filename):
    df = pd.read_csv(filename)

    getCountry(df)
    return df


#column namne sahi kro
#if all fields Nan toh delte the row


def getCountry(df):
    df1=df[1]
    