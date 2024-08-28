# try funciona para manejar excepciones (errores)

def verificar_range():
    r = range(10)

    try:
        r[0] = 5
        mutabilidad = True
    except TypeError:
        mutabilidad = False

    try:
        suma = r + r
        suma_valida = True
    except TypeError:
        suma_valida = False

    try:
        producto = r * 2
        producto_valido = True
    except TypeError:
        producto_valido = False

    try:
        slicing = r[2:5]
        slicing_valido = True
    except TypeError:
        slicing_valido = False

    try:
        lista = list(r)
        tupla = tuple(r)
        conversion_valida = True
    except TypeError:
        conversion_valida = False

    try:
        longitud = len(r)
        len_valido = True
    except TypeError:
        len_valido = False

    return {
        "mutabilidad": mutabilidad,
        "suma": suma_valida,
        "producto_por_entero": producto_valido,
        "slicing": slicing_valido,
        "conversion_a_lista_o_tupla": conversion_valida,
        "funcion_len": len_valido
    }

resultados = verificar_range()
for caracteristica, cumple in resultados.items():
    print(f"{caracteristica}: {'Cumple' if cumple else 'No cumple'}")
