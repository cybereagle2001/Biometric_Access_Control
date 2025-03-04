import os
import sys

x= "database"
fingerprints = os.listdir(x)

for loop in fingerprints:
    command = "sudo python3 app.py "+sys.argv[1]+" "+loop
    os.system(command)

