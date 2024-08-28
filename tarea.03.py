mi_diccionario = {
    'nombre': 'Marce',
    'edad': 20,
    'ciudad': 'Querétaro'
}
print(mi_diccionario)

edad = mi_diccionario.pop('edad')
print(f"Pop('edad'): {mi_diccionario}, valor eliminado: {edad}")

ciudad = mi_diccionario.get('ciudad')
print(f"Get 'ciudad': {ciudad}")

copia_diccionario = mi_diccionario.copy()
print(f"Copia: {copia_diccionario}")

claves = mi_diccionario.keys()
print(f"Claves: {list(claves)}")

items = mi_diccionario.items()
print(f"Items: {list(items)}")

mi_diccionario.clear()
print(f"Después de clear: {mi_diccionario}")

claves = ['a', 'b', 'c']
nuevo_diccionario = dict.fromkeys(claves, 0)
print(f"Nuevo diccionario fromkeys: {nuevo_diccionario}")

ultimo_item = nuevo_diccionario.popitem()
print(f"Popitem: {nuevo_diccionario}, item eliminado: {ultimo_item}")

valor = nuevo_diccionario.setdefault('d', 1)
print(f"Setdefault('d', 1): {nuevo_diccionario}, valor devuelto: {valor}")

nuevo_diccionario.update({'e': 2, 'f': 3})
print(f"Update: {nuevo_diccionario}")

valores = nuevo_diccionario.values()
print(f"Valores del diccionario: {list(valores)}")