import subprocess

subprocess.Popen('/usr/bin/gnome-calculator')

# We have the .poll() and .wait() methods for a subprocess object

# the Popen method also has a second argument for arguments you want to pass into the process
