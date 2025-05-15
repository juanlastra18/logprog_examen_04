import xml.etree.ElementTree as ET

#coding=utf-8 
# programa: Inventario de papeleria "EL pinguino escolar"
# autor: Juan Jose Lastra ID: 000492719

#Definicion de constantes Globales
categoria = ['utiles escolares', 'papeleria de oficina', 'Manualidades']
codigo_producto = ['UE001', 'UE002', 'PO001', 'PO002', 'MA001', 'MA002',]
nombre_producto = ['cuaderno cuadriculado', 'lapiz 2B', 'Resma Papel Carta', 'Carpeta Archivadora', 'Cartulina de Colores','Kit Pinturas Acuarela']
cantidad_producto = ['50', '120', '35', '25', '80','15']
precio_producto = ['3500', '800', '1200', '4500', '1200', '22000']
#PARA DEFINIR LA FUNCION DE MOSTRAR INVENTARIO SE TRABAJO SIGUIENDO LOS CONCEPTOS DE CLASES ANTERIORES Y SE REALIZO LA ADAPTACION DE LA FUNCION PARA QUE SE ADAPTARA A LA ESTRUCTURA DE INFORMACION PARA ESTE CODIGO
def mostrar_inventario(inventario):
    """
    Muestra el contenido del diccionario de inventario de papeleria

    Args:
        inventario (dict): Diccionario con el inventario de papeleria
    """
    print(f'\nTotal entradas: {len(inventario)}. Contenido del inventario:')
    for codigo, detalles in inventario.items():
        print(f'código: {codigo}')
        for atributo, valor in detalles.items():
            print(f'\t{atributo}: {valor}')

# LAS 3 FUNCIONES SIGUIENTES DE GUARDAR, LEER Y GENERAR, REALMENTE FUERON NO TAN COMPLICADAS DE TRABAJAR YA QUE SU ESTRUCTURA ES MUY SIMILAR, Y CON GUIA DE LOS PROYECTOS TRANAJADOS EN CLASE FUE SENCILLO, DONDE NOS PERMITIERON GUARDAR EL ARCHIVO XML, LEERLO Y GENERARLO
def guardar_archivo_xml(inventario, ruta_archivo):
    """
    Guarda el diccionario en un archivo XML
    Args:
        inventario (dict): Diccionario con el inventario de papeleria
        ruta_archivo (str): Ruta del archivo XML
    """
    nodo_raiz = ET.Element("papeleria") 

    for codigo, detalles in inventario.items():
        producto = ET.SubElement(nodo_raiz, "producto")
        producto.set("codigo", codigo)

        for campo, valor in detalles.items():
            atributo = ET.SubElement(producto, campo.lower())  
            atributo.text = str(valor)
    ET.indent(nodo_raiz, space="   ", level=0) 
    arbol_elementos = ET.ElementTree(nodo_raiz)
    arbol_elementos.write(ruta_archivo, encoding="utf-8", xml_declaration=True)
    print(f"El archivo XML ha sido guardado en {ruta_archivo}")

def leer_archivo_xml(ruta_archivo):
    """Lee un archivo XML y reconstruye el diccionario de inventario

    Args:
        ruta_archivo (str): Ruta del archivo XML con el inventario

    Returns:
        dict: Diccionario con el inventario de zapatos
    """
    inventario = {}

    arbol = ET.parse(ruta_archivo)
    nodo_raiz = arbol.getroot()

    for producto in nodo_raiz.findall('producto'):
        codigo = producto.get('codigo')

        datos_producto = {}
        for campo in producto:
            nombre_campo = campo.tag
            valor = campo.text
            if nombre_campo in ['cantidad', 'precio'] and valor.isdigit():
                valor = int(valor)
            datos_producto[nombre_campo] = valor
        inventario[codigo] = datos_producto

    return inventario

def generar_inventario(cantidad):
    """
    Genera un diccionario con el inventario de papeleria
    Args:
        cantidad (int): Cantidad de productos a generar
    returns:
        dict: Diccionario con el inventario de papeleria
    """
    inventario = {}

    for i in range(cantidad):
        codigo = codigo_producto[i]
        categoria_asignada = categoria[i % len(categoria)]  
        nombre = nombre_producto[i]
        cantidad = int(cantidad_producto[i])
        precio = int(precio_producto[i])

        inventario[codigo] = {
            'categoria': categoria_asignada,
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        }
#LA ESTRUCTURA DE ESTA FUNCION FUE MUY SIMILAR A LA TRABAJADA EN EL CODIGO JSON TENIENDO EN CUENTA LA CONFUSION EN ESTA PARTE DEL CODIGO, QUE FUE LA QUE MAS ME COSTO RALIZAR Y EN LA CUAL NECESITE APOYO DE IA
    return inventario

#funcion para aumentar el precio de los productos en un 8% USAMOS LA MISMA FUNCION PARA REALIZAR EL INCREMENTO PARA ESTE CODIGO Y EL JSON
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
#FUNCIÓN PARA AUMENTAR LA CANTIDAD DE LOS PRODUCTOS EN UN 12% USAMOS LA MISMA FUNCION PARA REALIZAR EL INCREMENTO PARA ESTE CODIGO Y EL JSON
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

def ejecutar_etapas(inventario, ruta_archivo, mensaje):
    print(f"\n{mensaje}")
    mostrar_inventario(inventario)
    guardar_archivo_xml(inventario, ruta_archivo)
    inventario = leer_archivo_xml(ruta_archivo)
    return inventario
#ESTA FUNCION LA CREE YA QUE EN LA PARTE DEL MAIN QUEDABA UN POCO CARGADA, INVESTIGUE UN POCO Y USE HERRAMIENTAS DE INTELIGENCIA ARTIFICIAL PARA PODER ENCONTRAR UNA MANERA DE EJECUTAR EL CODIGO, PERO TENIENDO UN MAIN UN POCO MAS LIMPIO Y NO TAN SATURADO


def main():
    """
    Funcion principal del programa
    """
    inventario = generar_inventario(6)
    inventario = ejecutar_etapas(inventario, "inventario.xml", "Inventario original:")
    inventario = aumentar_precio_inventario(inventario)
    inventario = ejecutar_etapas(inventario, "inventario_actualizado.xml", "Inventario con precios actualizados:")

    inventario = aumentar_cantidad_inventario(inventario)
    inventario = ejecutar_etapas(inventario, "inventario_actualizado_cantidad.xml", "Inventario con cantidades actualizadas:")

    print("\nPrograma finalizado.")
   

if __name__ == "__main__":
    
    main()
