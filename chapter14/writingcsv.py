#! /usr/bin/env python3

import csv

outputFile = open('output.csv', 'w', newline ='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

# delimiter and lineterminator keyword arguments
csvFile = open('example.tsv', 'w', newline = '')
csvWriter = csv.writer(csvFile, delimiter = '\t', lineterminator ='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()
