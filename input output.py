#string = input('Introduce una palabra: \n')

#print('Se recibió la cadena:', string, 'con tipo de dato', type(string))

#num = input('Introduce un número: \n')
#num = float(num)

#print('Se recibió el número:', num, 'con tipo de dato', type(num))

num = input('número:\n')
num = int(num)
pares = range(0, num+1, 2) # importante poner inicio, y rango no incluye el útimo valor (num)
print(sum(pares))