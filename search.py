import os
import sys

db= "database"
fingerprints = os.listdir(db)

for loop in fingerprints:
    command = "sudo python3 app.py "+sys.argv[1]+" "+loop
    exit_code = os.system(command)
    if exit_code == 0:
        print("Fingerprint matched. Stopping the Search.")
        break
