from datetime import datetime, timedelta
from time import sleep

# Obtener el momento actual
momento_actual = datetime.now()

# Esperar al menos 1 segundo
# Puedes usar la función sleep() del módulo time para esperar
# Asegúrate de importar time: from time import sleep
sleep(1)

# Definir un momento en el pasado o en el futuro después de esperar al menos 1 segundo
otro_momento = datetime.now()

# Calcular la diferencia de tiempo entre los dos momentos
variacion_temporal = otro_momento - momento_actual

# Imprimir la variación temporal
print("Variación temporal:", variacion_temporal)
