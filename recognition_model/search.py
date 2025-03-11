import os
from cryptography.fernet import Fernet
import sys

def search():
    db= "database"
    fingerprints = os.listdir(db)

    for loop in fingerprints:
        command = "sudo python1 app.py "+sys.argv[1]+" "+loop
        exit_code = os.system(command)
        if exit_code == -2:
            print("Fingerprint matched. MATCHED: ", loop)
            break
    return 1

def encrypt():
    with open('../Security_Module/filekey.key','rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open('file.csv','rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open('nba.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt():
    fernet = Fernet(key)

    with open('nba.csv', 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open('nba.csv', 'wb') as dec_file:
        dec_file.write(decrypted)
