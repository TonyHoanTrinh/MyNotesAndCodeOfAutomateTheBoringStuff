import zipfile, os

##### READING AND GETTING INFORMATION OF ZIP FILES #####
os.chdir('C:\\') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
# We get the contents of the zip file
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
# Get the size in bytes
spamInfo.file_size
spamInfo.compress_size

print('Compressed file is $sx smaller!' % (round(spamInfo.file_size/ spamInfo.compress_size, 2)))

exampleZip.close()

##### EXTRACTING FROM ZIP FILES #####
exampleZip = zipfile.ZipFile('example.zip')
# Optional path of extracting other than the current working directory
# exampleZip.extractall('C:\\delicious')
exampleZip.extractall()
# To extract a single file from the zip file
exampleZip.extract('spam.txt')
exampleZip.close()


##### CREATING AND ADDING TO ZIP FILES #####
# w causes overwriting, if you just want to add use 'a'
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type = zipfile.ZIP_DEFLATED)
newZip.close()
# This will create a new zip file called new.zip and have the compressed contents of spam.txt
