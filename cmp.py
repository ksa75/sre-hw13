import csv 
import json
import time

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray1 = []
    jsonArray2 = []
    cmp_area1 = []
    cmp_area2 = []
      
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray1.append(row)

    with open(jsonFilePath, encoding='utf-8') as jsonf:
        jsonArray2 = json.load(jsonf)
    
    for listItem in jsonArray1:
        for v in listItem.values():
            cmp_area1.append(v)
    
    for k,v in jsonArray2.items():
        if k == 'year':
            cmp_area2.append(str(v))        
        if k == 'months':
            for listItem in v:
                cmp_area2.append(listItem["days"])
        if k == 'statistic':
            for key,val in v.items():
                cmp_area2.append(str(val))
    print(cmp_area1)
    print(cmp_area2)
    print(f"Is identical: {cmp_area1 == cmp_area2}")
          
csvFilePath = r'calendar.csv'
jsonFilePath = r'calendar.json'

start = time.perf_counter()
csv_to_json(csvFilePath, jsonFilePath)
finish = time.perf_counter()

print(f"Conversion 100.000 rows completed successfully in {finish - start:0.4f} seconds")