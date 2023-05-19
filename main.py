import json
from datetime import datetime,date
hoy=datetime.now()
import os

# Ruta del directorio de base de datos
DB_DIR = "Base de Datos"
# Ruta del archivo de base de datos
DB_FILE = os.path.join(DB_DIR, "muestras.json")

# Función para cargar los datos desde el archivo JSON
def cargar_datos():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Función para guardar los datos en el archivo JSON
def guardar_datos(data):
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Función para validar la entrada de datos
def validar_entrada(entrada, tipo):
    while True:
        valor = input(entrada)
        if tipo == "int":
            if valor.isdigit():
                return int(valor)
            else:
                print("¡Error! Debes ingresar un valor numérico.")
        elif tipo == "str":
            if valor.isalpha() or valor.isalnum:
                return valor
            else:
                print("¡Error! Debes ingresar un valor alfabético.")

# Función para agregar una muestra al inventario
def agregar_muestra():
    nombre = validar_entrada("Ingrese el nombre del paciente: ", "str")
    documento = validar_entrada("Ingrese el documento de identidad del paciente: ", "int")
    codigo = validar_entrada("Ingrese el código de muestra: ", "str")
    responsable = validar_entrada("Ingrese el responsable de tomar la muestra: ", "str")
    fecha = hoy.strftime("%d-%m-%Y")
    eps = validar_entrada("Ingrese la EPS: ", "str")

    muestra = {
        "Nombre": nombre,
        "Documento": documento,
        "Código": codigo,
        "Responsable": responsable,
        "Fecha": fecha,
        "EPS": eps
    }

    inventario.append(muestra)
    guardar_datos(inventario)
    print("La muestra se ha agregado correctamente.")

# Función para mostrar el inventario de muestras
def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        print("Inventario de muestras:")
        for muestra in inventario:
            print("Nombre:", muestra["Nombre"])
            print("Documento:", muestra["Documento"])
            print("Código:", muestra["Código"])
            print("Responsable:", muestra["Responsable"])
            print("Fecha:", muestra["Fecha"])
            print("EPS:", muestra["EPS"])
            print("--------------------")

# Función para generar un informe en formato .txt
def generar_informe():
    if len(inventario) == 0:
        print("No hay muestras para generar el informe.")
    else:
        with open("informe.txt", "w") as file:
            file.write("Informe de muestras:\n")
            for muestra in inventario:
                file.write("Nombre: {}\n".format(muestra["Nombre"]))
                file.write("Documento: {}\n".format(muestra["Documento"]))
                file.write("Código: {}\n".format(muestra["Código"]))
                file.write("Responsable: {}\n".format(muestra["Responsable"]))
                file.write("Fecha: {}\n".format(muestra["Fecha"]))
                file.write("EPS: {}\n".format(muestra["EPS"]))
                file.write("--------------------\n")
                print("Se ha generado el informe correctamente.")

# Función para eliminar una muestra del inventario
def eliminar_muestra():
    codigo = validar_entrada("Ingrese el código de muestra a eliminar: ", "str")
    for muestra in inventario:
        if muestra["Código"] == codigo:
            inventario.remove(muestra)
            guardar_datos(inventario)
            print("La muestra se ha eliminado correctamente.")
            return
    print("No se encontró una muestra con el código ingresado.")

#Menú principal   
def menu():
    while True:
        print("=== Laboratorio - Gestión de Inventario ===")
        print("1. Agregar muestra")
        print("2. Mostrar inventario")
        print("3. Generar informe")
        print("4. Eliminar muestra")
        print("5. Salir")
        opcion = validar_entrada("Ingrese una opción: ", "int")
        print("-------------------------------------------")

        if opcion == 1:
            agregar_muestra()
        elif opcion == 2:
            mostrar_inventario()
        elif opcion == 3:
            generar_informe()
        elif opcion == 4:
            eliminar_muestra()
        elif opcion == 5:
            break
        else:
            print("¡Opción inválida! Por favor, ingrese una opción válida.")

#Carga de datos al inicio del programa
inventario = cargar_datos()
#iniciar
menu()