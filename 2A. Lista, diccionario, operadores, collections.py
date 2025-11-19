from collections import Counter, OrderedDict

#Colores 
VERDE = "\033[92m"
AZUL = "\033[94m"
AMARILLO = "\033[93m"
RESET = "\033[0m"

#Funciones 
def filtrar_clientes(compras, registrados):
    return list(set(compras) - set(registrados))

def eliminar_duplicados(compras):
    return list(OrderedDict.fromkeys(compras))

def contar_compras(compras):
    return Counter(compras)

def crear_resumen(conteo):
    return {c: f"Ha comprado {n} veces" for c, n in conteo.items() if n > 1}

#Función main
def main():
    # Datos de ejemplo
    compras = ["Luis", "Ana", "Luis", "Carlos", "Marta", "Ana", "Sofia",
    "Elena", "Luis", "Carlos"
    ]
    registrados = ["Ana", "Carlos", "Marta", "Elena"]

    # Ejecución de funciones
    nuevos = filtrar_clientes(compras, registrados)
    unicos = eliminar_duplicados(compras)
    conteo = contar_compras(compras)
    resumen = crear_resumen(conteo)

    # Impresión con colores
    print(f"\n{VERDE}CLIENTES NUEVOS NO REGISTRADOS{RESET}")
    print(nuevos)

    print(f"\n{AMARILLO}CLIENTES ÚNICOS{RESET}")
    print(unicos)

    print(f"\n{AZUL}CLIENTES FRECUENTES{RESET}")
    print(resumen)

#Patrón
if __name__ == "__main__":
    main()



