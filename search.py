import os
import sys

db= "database"
fingerprints = os.listdir(db)

for loop in fingerprints:
    command = "sudo python3 recognition_model/app.py "+sys.argv[1]+" "+loop
    os.system(command)

