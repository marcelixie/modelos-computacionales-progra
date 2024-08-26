my_list = ["ave", 1, "bolsa", 2, "casa", 3, "droga", 4, "eco", 5, "fuente", 6, "gato", 7, "historia", 8]

my_list.append("jicama")
print("Append:", my_list)

my_list.extend([9, "kaka", 10])
print("Extend:", my_list)

my_list.insert(2, "inserted_element")
print("Insert:", my_list)

my_list.remove("casa")
print("Remove:", my_list)

my_list.pop(3)
print("Pop:", my_list)

my_list.clear()
print("Clear:", my_list)

my_list = ["ave", 1, "bolsa", 2, "casa", 3, "droga", 4, "eco", 5, "fuente", 6, "gato", 7, "historia", 8] #volvemos a poner la lista porque la cleareamos unu

indice = my_list.index("droga")
print("Índice de 'droga':", indice)

count = my_list.count(2)
print("Count de 2:", count)

num = [2, 4, 6, 8, 1, 3, 5, 7, 9] #nueva lista para que jale sort
num.sort()
print("After sort", num)

my_list.reverse()
print("After reverse:", my_list)

copied_list = my_list.copy()
print("Copied list:", copied_list)