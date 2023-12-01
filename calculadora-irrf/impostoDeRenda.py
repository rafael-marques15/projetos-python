salario=float(input('Digite seu salário em reais: '))

if (salario<=1903.98):
    print('Você está isento do imposto de renda')
elif (salario>1903.98 and salario<=2836.65):
    imposto=salario*0.07
    print(f'Você vai pagar R$ {imposto:.2f} de imposto de renda')
elif (salario>2836.65 and salario<=3751.05):
    imposto=salario*0.15
    print(f'Você vai pagar R$ {imposto:.2f} de imposto de renda')
elif (salario>3751.05 and salario<=4664.68):
    imposto=salario*0.225
    print(f'Você vai pagar R$ {imposto:.2f} de imposto de renda')
elif (salario>4664.68):
    imposto=salario*0.275
    print(f'Você vai pagar R$ {imposto:.2f} de imposto de renda')
else:
    print('Por favor, digite um valor válido')