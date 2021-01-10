import shutil, os
os.chdir('C:\\')
# shutil.copy(source, destination)
# If the destination is the filename, the source will be renamed that when copied over
shutil.copy('C:\\spam.txt', 'C"\\delicious')
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
# shutil.copytree(source, destination)
shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
