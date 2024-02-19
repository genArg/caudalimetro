from datetime import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.now()

# Imprimir la fecha y hora actual
#print("Fecha y hora actual:", fecha_hora_actual)

# Formatear la fecha y hora actual como una cadena
fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
print("Fecha y hora formateada:", fecha_hora_formateada)
