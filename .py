import json

#coding=utf-8 
# programa: Inventario de papeleria "EL pinguino escolar"
# autor: Juan Jose Lastra ID: 000492719

#Definicion de constantes Globales
categoria = ['utiles escolares', 'papeleria de oficina', 'Manualidades']
codigo_producto = ['UE001', 'UE002', 'PO001', 'PO002', 'MA001', 'MA002',]
nombre_producto = ['cuaderno cuadriculado', 'lapiz 2B', 'Resma Papel Carta', 'Carpeta Archivadora', 'Cartulina de Colores','Kit Pinturas Acuarela']
cantidad_producto = ['50', '120', '35', '25', '80','15']
precio_producto = ['3500', '800', '1200', '4500', '1200', '22000']
ARCHIVO_INVENTARIO_JSON = 'inventario_papeleria.json'

#Creamos la primera funcion para mostrar el inventario, trabajandolo muy similar a como lo hemos venido trabajando en clase en ejemplos como el programa de bicicletas y zapatos.
def mostrar_inventario(inventario):
    """
    Muestra el contenido del diccionario de inventario de papelería

    Args:
        inventario (dict): Diccionario con el inventario de papelería
    """
    print(f'\nTotal entradas: {len(inventario)}. Contenido del inventario:')
    for codigo, detalles in inventario.items():
        print(f'Código: {codigo}')
        for atributo, valor in detalles.items():
            print(f'\t{atributo}: {valor}')

# funcion para generar el inventario con los 6 productos definidos en el orden original, esta funcion fue la que mas me costo realizar,Use apoyo de IA (chapgpt) para poder realizar esta funcion, ya que la hice de varias formas y ninguna funcionaba como lo pedia el ejercicio, al comienzo los codigos de los productos se generaban de forma aleatoria, luego intentando de otra forma me generaba el inventario pero con los codigos de los productos repetidos y no salian todos los productos, asi que con IA logre realizarla y entendi que la forma mas sencilla era crear una funcion con un inventario ya establecido. 
def generar_inventario_definido():
    """
    Genera el inventario con los 6 productos definidos en el orden original
    Returns:
        dict: Inventario con estructura completa y códigos correctos
    """
    categorias_asignadas = [
        'utiles escolares', 'utiles escolares',
        'papeleria de oficina', 'papeleria de oficina',
        'Manualidades', 'Manualidades'
    ]

    inventario = {}

    for i in range(len(codigo_producto)):
        codigo = codigo_producto[i]
        inventario[codigo] = {
            'categoria': categorias_asignadas[i],
            'nombre': nombre_producto[i],
            'cantidad': int(cantidad_producto[i]),
            'precio': int(precio_producto[i])
        }
    return inventario

# con esta funcion guardamos el inventario en un archivo json, con una estructura muy similar a la trabajada en clase, en el programa de bicicletas y zapatos.
def guardar_inventario_json(inventario,ruta_archivo):
    """
    Guarda el diccionario de inventario en un archivo JSON
    Args:
    inventario (dict): Diccionario con el inventario de papeleria
    ruta_archivo (str): Ruta del archivo JSON donde se guardará el inventario
    """
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo_destino:
            json.dump(inventario, archivo_destino, indent=4, ensure_ascii=False)

        print(f"Archivo '{ruta_archivo}' creado exitosamente.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")
# funcion para leer el inventario desde el archivo json, con una estructura muy similar a la trabajada en clase, en el programa de bicicletas y zapatos.
def leer_inventario_json(ruta_archivo):
    """
    Lee un archivo JSON y reconstruye el diccionario de inventario
    Args:
        ruta_archivo (str): Ruta del archivo JSON con el inventario

    Returns:
        dict: Diccionario con el inventario de papeleria
    """
# Esta parte del programa tambien se realizo de una forma similar a la trabajada en clase, en el programa de bicicletas y zapatos.Pero aca tuve cierta dificultad por un error muy basico ya qe estaba colocandi el except exception como el primero y no como el ultimo, lo cual me generaba un error
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_origen:
            diccionario = json.load(archivo_origen)
        print(f"Archivo '{ruta_archivo}' leído exitosamente.")
        return diccionario
    except FileNotFoundError as fnfe:
       print(f"Error al leer el archivo: {fnfe}")
       return {}
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    

#funcion para aumentar la cantidad de los productos en un 12%
def aumentar_cantidad_inventario(inventario):
    """
    Aumenta la cantidad de los productos en un 12%
    Args:
        inventario (dict): Diccionario con la cantidad de papeleria
    """
    for codigo, detalles in inventario.items():
        cantidad_actual = int(detalles['cantidad'])
        nueva_cantidad = int(cantidad_actual) * 1.12 
        detalles['cantidad'] = int(nueva_cantidad)
    print("Las cantidades han sido actualizadas correctamente.")
    return inventario

#funcion para aumentar el precio de los productos en un 8%
def aumentar_precio_inventario(inventario):
    """
    Aumenta el precio de los productos en un 8%
    Args:
        inventario (dict): Diccionario con el precio de papeleria
    """
    for codigo, detalles in inventario.items():
        precio_actual = int(detalles['precio'])
        nuevo_precio = int(precio_actual * 1.08)  
        detalles['precio'] = nuevo_precio
    print("Los precios han sido actualizados correctamente.")
    return inventario


def main():
    """
    Funcion principal del programa
    """
   

    # Generar un inventario aleatorio con 6 productos
    inventario = generar_inventario_definido()
    print("\n Inventario generado aleatoriamente:")
    mostrar_inventario(inventario)
   
    #Guardar en JSON
    guardar_inventario_json(inventario, ARCHIVO_INVENTARIO_JSON)
    
    #Leer el inventario desde el archivo
    inventario = leer_inventario_json(ARCHIVO_INVENTARIO_JSON)
    mostrar_inventario(inventario)
    print("\n Inventario leído desde el archivo:")
    mostrar_inventario(inventario)

    #Aumentar la cantidad un 12%
    aumentar_cantidad_inventario(inventario)
    print("\n Inventario después de aumentar la cantidad un 12%:")
    mostrar_inventario(inventario)

    #Aumentar el precio un 8%
    aumentar_precio_inventario(inventario)
    print("\n Inventario después de aumentar el precio un 8%:")
    mostrar_inventario(inventario)

    #Guardar los cambios nuevamente en JSON
    guardar_inventario_json(inventario, ARCHIVO_INVENTARIO_JSON)
    print("\n El inventario actualizado se ha guardado correctamente en el archivo JSON.")
if __name__ == "__main__":
    
    main()
