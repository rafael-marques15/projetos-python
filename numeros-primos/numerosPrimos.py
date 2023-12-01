numero=int(input('Digite o número que você deseja saber os primos: '))
for n in range (1,numero+1):
    restoDiv= numero%n
    if (restoDiv==0):
        print(f' {n} é primo de {numero}')
    
    