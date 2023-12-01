altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))
imc = peso/(altura*altura)

if (imc<18.5):
    print(f'Seu IMC é {imc:.2f}, e você está abaixo do peso, procure se alimentar melhor!')
elif(imc>=18.5 and imc<=24.9):
    print(f'Seu IMC é {imc:.2f}, e você está no peso ideal, continue assim!')
elif(imc>=25.0 and imc<=29.9):
    print(f'Seu IMC é {imc:.2f}, e você está levemente acima do peso, procure fazer exercícios e melhorar a alimentação!')
elif(imc>30.0):
    print(f'Seu IMC é {imc:.2f}, e você está com obesidade, procure ajuda médica!')