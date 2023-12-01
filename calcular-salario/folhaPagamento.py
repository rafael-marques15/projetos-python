import salarioMensal
vt=salarioMensal.salarioMensal*0.06
if (salarioMensal.salarioMensal >= 0.01 and salarioMensal.salarioMensal <= 1302.00):
    inss= salarioMensal.salarioMensal*0.075
    salarioLiquido= salarioMensal.salarioMensal-inss-vt
    print(f'''\n
 ________________________________
|
|-------Folha de pagamento-------
|          
| Nome: {salarioMensal.nome}
| Salário bruto: R$ {salarioMensal.salarioMensal:.2f}
|
|-----------Descontos------------
|
| INSS: R$ {inss:.2f}
| VT: R$ {vt:.2f}
|--------------------------------
| Salário Líquido: R$ {salarioLiquido:.2f}
|________________________________\n''')
elif (salarioMensal.salarioMensal>=1302.01 and salarioMensal.salarioMensal<=2571.29):
    inss= salarioMensal.salarioMensal*0.09
    salarioLiquido= salarioMensal.salarioMensal-inss-vt
    print(f'''\n
 ________________________________
|
|-------Folha de pagamento-------
|          
| Nome: {salarioMensal.nome}
| Salário bruto: R$ {salarioMensal.salarioMensal:.2f}
|
|-----------Descontos------------
|
| INSS: R$ {inss:.2f}
| VT: R$ {vt:.2f}
|--------------------------------
| Salário Líquido: R$ {salarioLiquido:.2f}
|________________________________\n''')
elif (salarioMensal.salarioMensal>=2571.30 and salarioMensal.salarioMensal<= 3856.94):
    inss= salarioMensal.salarioMensal*0.12
    salarioLiquido= salarioMensal.salarioMensal-inss-vt
    print(f'''\n
 ________________________________
|
|-------Folha de pagamento-------
|          
| Nome: {salarioMensal.nome}
| Salário bruto: R$ {salarioMensal.salarioMensal:.2f}
|
|-----------Descontos------------
|
| INSS: R$ {inss:.2f}
| VT: R$ {vt:.2f}
|--------------------------------
| Salário Líquido: R$ {salarioLiquido:.2f}
|________________________________\n''')

elif (salarioMensal.salarioMensal>=3856.95 and salarioMensal.salarioMensal<=7507.49):
    inss= salarioMensal.salarioMensal*0.14
    salarioLiquido= salarioMensal.salarioMensal-inss-vt
    print(f'''\n
 ________________________________
|
|-------Folha de pagamento-------
|          
| Nome: {salarioMensal.nome}
| Salário bruto: R$ {salarioMensal.salarioMensal:.2f}
|
|-----------Descontos------------
|
| INSS: R$ {inss:.2f}
| VT: R$ {vt:.2f}
|--------------------------------
| Salário Líquido: R$ {salarioLiquido:.2f}
|________________________________\n''')
else:
    teto=877.22
    salarioLiquido= salarioMensal.salarioMensal-teto-vt
    print(f'''\n
 ________________________________
|
|------Folha de pagamento-------
|          
| Nome: {salarioMensal.nome}
| Salário bruto: R$ {salarioMensal.salarioMensal:.2f}
|
|----------Descontos------------
|
| INSS: R$ {teto:.2f}
| VT: R$ {vt:.2f}
|-------------------------------
| Salário Líquido: R$ {salarioLiquido:.2f}
|________________________________\n''')
