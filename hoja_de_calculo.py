from openpyxl import Workbook

# Crear un nuevo libro de trabajo (workbook)
workbook = Workbook()

# Seleccionar la hoja activa (por defecto la primera hoja)
sheet = workbook.active

# Cambiar el nombre de la hoja de cálculo
sheet.title = "MiHojaDeCalculo"

# Agregar datos a la hoja de cálculo
sheet['A1'] = 'Nombre'
sheet['B1'] = 'Edad'

datos = [
    ('Alice', 30),
    ('Bob', 35),
    ('Charlie', 25)
]

for nombre, edad in datos:
    sheet.append([nombre, edad])

# Guardar el libro de trabajo en un archivo
workbook.save(filename='datosjaja.xlsx')
