numero=1
print(f'\nA tabuada do {numero} é: \n')
for n in range (0,11):
    multiplicador=numero*n
    print(f'{numero} x {n} = {multiplicador}')

for x in range (0,9):
    numero= numero+1
    print(f'\nA tabuada do {numero} é: \n')
    for n in range (0,11):    
        multiplicador=numero*n
        print(f'{numero} x {n} = {multiplicador}')
    