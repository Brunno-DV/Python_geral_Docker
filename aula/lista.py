numeros = [1,2,3,4,5]
print('Lista de números:', numeros)
print('Primeiro número:', numeros[1])
print('Último elemento:', numeros[-1])

numeros.append(6)
'''print('Lista de números:', numeros)
print('Primeiro número:', numeros[1])
print('Último elemento:', numeros[-1])'''

for numero in numeros:
    print(numero)

if 2 in numeros:
    print('O número 2 está na lista')
else:
    print('O número 2 não está na lista')