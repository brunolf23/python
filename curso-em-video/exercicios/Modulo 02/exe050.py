# Soma dos pares

soma = 0
cont = 0
for i in range (1, 7):
    numero = int(input(f'Digite o {i} valor: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print (f'Você informou {cont} número(s) par(es) e a soma foi {soma}.')