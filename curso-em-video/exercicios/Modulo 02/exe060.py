# Cálculo do Fatorial

numero = int(input('Digite um número para calcular seu fatorial: '))
c = numero
f = 1

print (f'Calculando {numero}! = ', end='')
while c > 0:
    print (f'{c}', end='')
    print (' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print (f'{f}')