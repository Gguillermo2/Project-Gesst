import random
import bcrypt
import getpass
from cryptography.fernet import Fernet

from Modelo.models import AdminUser

Admin = AdminUser


# Funciones para generar usuario y Contraseña maestras


def generar_Admin():
    NombreAdmin = input("Ingrese su nombre de usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ")
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    password = hashed

    nuevoadmin = AdminUser(
        username= NombreAdmin,
        ContresañUser = password

    )

    return nuevoadmin


usuario = generar_Admin()

print(f"el usuario es {usuario}")




