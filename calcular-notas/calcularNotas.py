nome=str(input('Digite seu nome: '))
ra=str(input('Digite seu RA: '))
atividade1 = float(input('Digite sua nota da N1: '))
atividade2 = float(input('Digite sua nota da N2: '))
provaFinal = float(input('Digite sua nota da prova final: '))
pesoProvaFinal = (provaFinal * 0.6)
pesoAtividades= (atividade2+atividade1)/5
mediaFinal = (pesoAtividades + pesoProvaFinal)
boletim=f""" __________________________________
|
| -----------Boletim------------
|
| Aluno: {nome}
| Matrícula: {ra}
| Nota N1: {pesoAtividades:.2f}
| Nota N2: {pesoProvaFinal:.2f}
| Média final: {mediaFinal:.2f}
| -------------------------------""";
if(mediaFinal >= 7):
    print(boletim)
    print('''| Parabéns, você foi aprovado!!! :)
|__________________________________\n''')
elif (mediaFinal >= 5 and mediaFinal < 7):
    print(boletim)
    print('''| Vai precisar fazer prova de recuperação :/
|__________________________________\n''')
else:
    print(boletim)
    print('''| Infelizmente você reprovou :(    
|__________________________________\n''')