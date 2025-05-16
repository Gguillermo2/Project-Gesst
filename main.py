from core import seguridad

def main():
        usuario = seguridad.generar_Admin()
        print(f"El usuario generado es {usuario}")

if __name__ == "__main__":
        main()