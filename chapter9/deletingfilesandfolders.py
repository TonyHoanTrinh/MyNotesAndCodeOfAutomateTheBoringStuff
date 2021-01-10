import os
# Calling os.unlink(path) will delete the file at path
# Calling os.rmdir(path) will delete the folder at path. The folder must be empty of any files or folders.
# Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)
        # os.unlick(filename)
