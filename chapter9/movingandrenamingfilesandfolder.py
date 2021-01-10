import shutil
# shutil.move(source, destination)
shutil.move('C:\\bacon.txt', 'C:\\eggs')
# If destination is a filename, the file moved will be renamed to that
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
# If there is not folder called eggs already in our destination
# Then it move the source with the name of the destination
shutil.move('C:\\bacon.txt', 'C:\\eggs')
# If there is no eggs folder then the path would become C:\\eggs

