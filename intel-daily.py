import json
from intelxapi import intelx
import csv
import ast
import re
from datetime import datetime, timedelta

now = datetime.now()

enddate = now.strftime("%Y-%m-%d %H:%M:%S")

enddate_datetime = datetime.strptime(enddate, "%Y-%m-%d %H:%M:%S")
startdate_datetime = enddate_datetime - timedelta(hours=CHANGEME) # eg 24/48/60

startdate = startdate_datetime.strftime("%Y-%m-%d %H:%M:%S")


b = ['CHANGEME'] #Bucket Lists eg 'darknet', 'leaks.public', 'leaks.private'
company_list = []

intelx = intelx('CHANGEME') #Your API key
f = open(f"/CHANGEME/{enddate}.txt", "a+") #Path you want to write file to 

for company in company_list:

    results = intelx.search(company, maxresults=200, buckets=b, datefrom=startdate, dateto=enddate)
    for i in results['records']:
        result = i
        contents = intelx.FILE_VIEW(result['type'], result['media'], result['storageid'], result['bucket'])


        lines_with_company_name = []

        for line in contents.split('\n'):
            if company in line:
                lines_with_company_name.append(line)


        for line in lines_with_company_name:

            f.write(line)

f.close()

