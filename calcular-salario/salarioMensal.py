nomeCompleto=str(input('Digite seu nome: '))
tipoSalario=str(input('Digite "M" se você recebe por mês, ou "H" se você recebe por hora: '))

if(tipoSalario=='M' or tipoSalario=='m'):
    salarioMensal=float(input('Digite seu salário mensal: '))
elif(tipoSalario=='H' or tipoSalario=='h'):
    diasTrabalhados=int(input('Digite a quantidade de dias trabalhados: '))
    salarioHora=float(input('Digite seu salário por hora: '))
    horasTrabalhadas=int(input('Digite a quantidades de horas trabalhadas por dia: '))
    salarioDia=salarioHora*horasTrabalhadas
    salarioMensal=salarioDia*diasTrabalhados
    print(f'Seu salário desse mês será no valor de R$ {salarioMensal} ')