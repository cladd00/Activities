import os 
import csv

csv_path = os.path.join('.','Resources', 'cereal.csv')
with open(csv_path, newline = '') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    for row in csv_reader:
        if(float(row[7]) >= 5):
            print(row)


            