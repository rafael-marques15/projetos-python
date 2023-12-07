import salarioMensal

if (salarioMensal.salarioMensal<=1903.98):
    imposto=0
    print('Você está isento do imposto de renda')
elif (salarioMensal.salarioMensal>1903.98 and salarioMensal.salarioMensal<=2836.65):
    imposto=salarioMensal.salarioMensal*0.07
    print(f'Você vai pagar R$ {imposto:.2f} de imposto de renda')
elif (salarioMensal.salarioMensal>2836.65 and salarioMensal.salarioMensal<=3751.05):
    imposto=salarioMensal.salarioMensal*0.15
    print(f'Você vai pagar R$ {imposto:.2f} de imposto de renda')
elif (salarioMensal.salarioMensal>3751.05 and salarioMensal.salarioMensal<=4664.68):
    imposto=salarioMensal.salarioMensal*0.225
    print(f'Você vai pagar R$ {imposto:.2f} de imposto de renda')
elif (salarioMensal.salarioMensal>4664.68):
    imposto=salarioMensal.salarioMensal*0.275
    print(f'Você vai pagar R$ {imposto:.2f} de imposto de renda')
else:
    print('Por favor, digite um valor válido')