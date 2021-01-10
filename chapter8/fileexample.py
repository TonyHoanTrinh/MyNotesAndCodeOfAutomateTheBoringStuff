import os
print(os.path.join('usr', 'bin', 'spam'))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/Users/quochoantrinh', filename))

print(os.getcwd())
# We can also use os.chdir() to change the directory

# We can create new folders like this
# os.makedirs('C:\\delicious\\walnut\\waffles')

# We can use the os.path module and its fnction
# We can get the absolute path from a relative path
print(os.path.abspath('.'))
# Or check if a path is absolute or not os.path.isabs('.')

# We can also have relpath (path, start) where it will return a string of the path from start path to path
# print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))

# Getting just the directory name and the base name 
path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print('/usr/bin'.split(os.path.sep))

# Getting the byte size of the file in the path
print(os.path.getsize(os.getcwd()))
# Getting the names of each file in the path argument
print(os.listdir(os.getcwd()))

# Check if path exists
print(os.path.exists('C:\\Windows'))
# Check if path is a file or folder
print(os.path.isdir('C:\\Windows\\System32'))
print(os.path.isfile('C:\\Windows\\System32'))

# Opening/Reading Files
helloFile = open('hello.txt', 'r')
helloContent = helloFile.read()
print(helloContent)
helloFile.close()
sonnetFile = open('sonnet29.txt')
print(sonnetFile.readlines())
sonnetFile.close()

# Writing files
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello World!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
