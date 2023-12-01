numero1 = float(input('\nDigite um número: '))
numero2 = float(input('Digite outro número: '))
operacao = str(input('''\nDigite a operacao desejada:
Para soma : "+"  
Para subtração : "-" 
Para multiplicação : "*" 
Para divisão : "/"
'''))
if (operacao == '+'):
    soma=numero1+numero2
    print(f'\n{numero1:.2f} + {numero2:.2f} = {soma:.2f}\n')
elif (operacao == '-'):
    subtracao=numero1-numero2
    print(f'\n{numero1:.2f} - {numero2:.2f} = {subtracao:.2f}\n')
elif (operacao == '*'):
    multiplicacao=numero1*numero2
    print(f'\n{numero1:.2f} x {numero2:.2f} = {multiplicacao:.2f}\n')
elif (operacao == '/'):
    divisao=numero1/numero2
    print(f'\n{numero1:.2f} : {numero2:.2f} = {divisao:.2f}\n')
else:
    print(f'\nDigite um caractere válido para a operação\n')