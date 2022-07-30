#!/bin/sh

echo Add Changes
$ chmod 777 webscraper.py
$ python webscraper.py

echo Get Differences

$ chmod 777 getDiff.py
$ python getDiff.py

echo Upload Differences

$ chmod 777 uploadData.py
$ python uploadData.py