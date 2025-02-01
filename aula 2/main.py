print('ex 1')
numero = int(input("digite um numero: "))

if numero % 2 == 0:
    print('par')
else:
    print('impar')
print('fim')

print('ex 2')
numero = int(input("digite um numero: "))

if numero > 0:
    print('positivo')
elif numero < 0:
    print('negativo')
else:
    print('zero')

print('ex 3')
numero1 = int(input("digite um numero: "))
numero2 =int(input("digite outro numero: "))

if numero1 > numero2:
    print(f'{numero1} é maior que o  {numero2}')
elif numero2 > numero1:
    print(f'{numero2} é maior que o  {numero1}')
else:
    print('é igual')
