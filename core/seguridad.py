import random
import os
import bcrypt
from cryptography.fernet import Fernet

# --------------------  encriptacion y desencriptacion ----------------------------- #
# Variables con instancias para su utilizacion
KEY_FILE = "key.key"
DATA_FILE = "baseDatos.json"

# Funcion para generar clave secreta
def GeneracionArch_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as keyfile:
            keyfile.write(key)
# funcion que carga y lee la clave para su utilizacion
def LeerArch_key():
    with open(KEY_FILE, "rb") as keyfile:
        return keyfile.read()
    

GeneracionArch_key()
key = LeerArch_key()
cipher = Fernet(key)

def generar_Codigo():
    return "".join(str(random.randint(0,9)) for o in range(5))

''' para encriptar pero se hace mas faci dentro de la misma funcion
def encriptacionP(Password_cryp):
    return cipher.encrypt(Password_cryp.encode()).decode()
'''
def desencrypt(Encrytep_has):
    return cipher.decrypt(Encrytep_has.encode()).decode()










