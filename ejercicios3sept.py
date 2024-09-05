# 1) Create a function that get a integer and calculate the factorial of
# that number (a non-negative integer)
#
# fact = int(input('ingresa un número mayor a 1\n'))
# Fact = fact
# while fact>1:
#     Fact= Fact*(fact-1)
#     fact = fact-1
# # if 0<=fact<=1:
# #     Fact = 1
#
# print('El factorial es', Fact)

# alternativa
# if int<0:
#     print('No existe')
# resultado = 1
# for i in range(1,int+1):
#     resultado*=i
#
# print(resultado)


# 2) Create a function that receives 3 numbers and verify if the third number is
# between the 2 first numbers
# def checar(a, b, c):
#     if a<=c<=b:
#         print('YES')
#     else : print('NO')
#
# checar(1,3,-10)

# 3) Given a string, create 2 functions to count the number of spaces in the string
# string = (' hola  mi nombre es marce')
# def espacio(string):
#     list = string.split()
#     print('el numero de espacios es:' , len(list) - 1)

# espacio(string)

# def space(string):
#     contador = 0
#     for i in range(len(string)):
#         if string[i] == ' ':
#           contador += 1
#         else: continue
#     print(contador)

#  alternativaa no ocupo el for,,, o si???????
# def space(string):
#     contador = 0
#     if string[i] == ' ':
#         contador += 1
#     print(contador)
# space(string)

# alternativa 2 bien facil lol
# num_espacios = string.count(' ')

# 4) Given a list, create a function to print the odd numbers in the list
# lista = [1,2,3,4,5,6,7,8,9, 11.5]
# def impares(lista):
#     imp = [ ]
#     for i in range(len(lista)):
#         if lista[i] %2 == 1:
#           imp.append(lista[i])
#         else: continue
#     print (imp)
#
# impares(lista)


# def factoria(valor):
#     if valor<1:
#         return 1
#     return valor * factoria(valor-1)
#
# print(factoria(5))
