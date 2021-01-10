#! /usr/bin/env python3

import csv
exampleFile = open('./Automate_online-materials/example.csv')
exampleReader = csv.reader(exampleFile)
'''
exampleData = list(exampleReader)
print(exampleData)

# You can read it with row and col index. Where row is the index of the list
# And col is the index of the item in that particular list
print(exampleData[0][0])
print(exampleData[6][1])
'''

# It is a good idea to read in csv files with a loop to avoid loading
# the entire file into memory at once
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
