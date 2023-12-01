from math import sqrt

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = pow(b, 2) - (4 * a * c)

if delta < 0:
    print('Delta é negativo. A equação não possui raízes reais.')
elif delta == 0:
    x = (-b) / (2 * a)
    print(f'O delta é igual a {delta} ,X é igual a {x:.2f}.')
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'Delta é igual a {delta}, X1 é igual a {x1:.2f} e X2 é igual a {x2:.2f}.')
