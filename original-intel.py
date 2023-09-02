import json
from intelxapi import intelx
import csv
import ast
import re

startdate = "CHANGEME" #Start date (2023-08-30 23:59:59)
enddate = "CHANGEME"   #End date (2023-08-30 23:59:59)


b = ['CHANGEME'] #Leaks Buckest ('darknet', 'leaks.public', 'leaks.private')
company_list = ['CHANGEME']  #Company List
intelx = intelx('CHANGEME') #Your intelx API key
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
            print(line)





