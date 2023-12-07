import salarioMensal
import impostoDeRenda
vt=salarioMensal.salarioMensal*0.06
if (salarioMensal.salarioMensal >= 0.01 and salarioMensal.salarioMensal <= 1302.00):
    inss= salarioMensal.salarioMensal*0.075
    salarioLiquido= salarioMensal.salarioMensal-inss-vt-impostoDeRenda.imposto
    print(f'''\n
 ________________________________
|
|-------Folha de pagamento-------
|          
| Nome completo: {salarioMensal.nomeCompleto}
| Salário bruto: R$ {salarioMensal.salarioMensal:.2f}
|
|-----------Descontos------------
|
| IRRF: R$ {impostoDeRenda.imposto:.2f}
| INSS: R$ {inss:.2f}
| VT: R$ {vt:.2f}
|--------------------------------
| Salário Líquido: R$ {salarioLiquido:.2f}
|________________________________\n''')
elif (salarioMensal.salarioMensal>=1302.01 and salarioMensal.salarioMensal<=2571.29):
    inss= salarioMensal.salarioMensal*0.09
    salarioLiquido= salarioMensal.salarioMensal-inss-vt-impostoDeRenda.imposto
    print(f'''\n
 ________________________________
|
|-------Folha de pagamento-------
|          
| Nome: {salarioMensal.nomeCompleto}
| Salário bruto: R$ {salarioMensal.salarioMensal:.2f}
|
|-----------Descontos------------
|
| IRRF: R$ {impostoDeRenda.imposto:.2f}
| INSS: R$ {inss:.2f}
| VT: R$ {vt:.2f}
|--------------------------------
| Salário Líquido: R$ {salarioLiquido:.2f}
|________________________________\n''')
elif (salarioMensal.salarioMensal>=2571.30 and salarioMensal.salarioMensal<= 3856.94):
    inss= salarioMensal.salarioMensal*0.12
    salarioLiquido= salarioMensal.salarioMensal-inss-vt-impostoDeRenda.imposto
    print(f'''\n
 ________________________________
|
|-------Folha de pagamento-------
|          
| Nome: {salarioMensal.nomeCompleto}
| Salário bruto: R$ {salarioMensal.salarioMensal:.2f}
|
|-----------Descontos------------
|
| IRRF: R$ {impostoDeRenda.imposto:.2f}
| INSS: R$ {inss:.2f}
| VT: R$ {vt:.2f}
|--------------------------------
| Salário Líquido: R$ {salarioLiquido:.2f}
|________________________________\n''')

elif (salarioMensal.salarioMensal>=3856.95 and salarioMensal.salarioMensal<=7507.49):
    inss= salarioMensal.salarioMensal*0.14
    salarioLiquido= salarioMensal.salarioMensal-inss-vt-impostoDeRenda.imposto
    print(f'''\n
 ________________________________
|
|-------Folha de pagamento-------
|          
| Nome: {salarioMensal.nomeCompleto}
| Salário bruto: R$ {salarioMensal.salarioMensal:.2f}
|
|-----------Descontos------------
|
| IRRF: R$ {impostoDeRenda.imposto:.2f}
| INSS: R$ {inss:.2f}
| VT: R$ {vt:.2f}
|--------------------------------
| Salário Líquido: R$ {salarioLiquido:.2f}
|________________________________\n''')
else:
    inss=877.22
    salarioLiquido= salarioMensal.salarioMensal-inss-vt-impostoDeRenda.imposto
    print(f'''\n
 ________________________________
|
|------Folha de pagamento-------
|          
| Nome: {salarioMensal.nomeCompleto}
| Salário bruto: R$ {salarioMensal.salarioMensal:.2f}
|
|----------Descontos------------
|
| IRRF: R$ {impostoDeRenda.imposto:.2f}
| INSS: R$ {inss:.2f}
| VT: R$ {vt:.2f}
|-------------------------------
| Salário Líquido: R$ {salarioLiquido:.2f}
|________________________________\n''')
