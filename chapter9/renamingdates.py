#! /usr/bin/env python3
# renamingdates.py - renames filenames with American MM-DD-YYYY data format to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American data format
dataPattern = re.compile(r"""^(.*?) # all text before the data
        ((0|1)?\d)-                 # one or two digits for the month
        ((0|1|2|3)?\d)-             # one or two digits for the day 
        ((19|20)\d\d)               # four digits for the year
        (.*?)$                      # all text after the data
        """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = dataPettern.search(amerFilename)
    
    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)


    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename) # uncomment after testing



