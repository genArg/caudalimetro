import subprocess
import sys

def verificar_instalacion(modulo):
    try:
        __import__(modulo)
    except ImportError:
        print(f"{modulo} no está instalado. Instalándolo ahora...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", modulo])
        print(f"{modulo} instalado exitosamente.")

# Lista de módulos a verificar e instalar si es necesario
modulos_a_verificar = [
    "tkinter",
    "openpyxl",
    "datetime",
    "threading",
    "collections"
]

# Verificar e instalar cada módulo
for modulo in modulos_a_verificar:
    verificar_instalacion(modulo)

## intalacion de un paquete
#pip install nombre_del_modulo
   
## desintalacion de un paquete
#pip uninstall nombre_del_modulo