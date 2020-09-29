"""
Proyecto Python y MySQL
-Abrir asistente
-Login o registro
-Si elegimos registro creará un usuario en la base de datos
-Si elegimos login indentificará al usuario y nos preguntará
-Crear nota, mostrar nota, borrarlas.
"""
#Importar paquetes:
from usuarios import acciones
#Imprimir en pantalla las primeras acciones a realizar:
print(""" 
ACCIONES DISPONIBLES:
    - Registro
    - Login
""")
#-------------------------------------------------------
#Asignar a la variable"hazEl" la clase acciones del módulo acciones del paquete usuarios.
hazEl = acciones.Acciones()
#-------------------------------------------------------
#Programa pregunta la acción a realizar y la guarda en la variable "accion"
accion = input("¿Qué desea hacer? ")
#-------------------------------------------------------
#Mediante la condicional if el programa decide si se ejecuta el bloque de acciones de registro o login
#ambos bloques de acciones se encuentran en el paquete usuarios en la clase acciones.
if accion.lower() == "registro":
    hazEl.registro()
elif accion.lower() == "login":
    hazEl.login()

