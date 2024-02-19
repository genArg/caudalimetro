import serial
from serial.threaded import ReaderThread

class MyProtocol(serial.threaded.Protocol):
    def data_received(self, data):
        # Manejar los datos recibidos
        print("Datos recibidos:", data)

# Configurar el puerto serial
port = serial.Serial('/dev/ttyUSB0', baudrate=9600)

# Configurar el lector de hilos
reader = ReaderThread(port, MyProtocol)

# Iniciar la recepción de datos en segundo plano
reader.start()

# Realizar otras operaciones mientras se reciben datos en segundo plano
while True:
    # Hacer otras cosas aquí...
    pass
