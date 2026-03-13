# ESTRUTURAS CONDICIONAIS

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print("Você é menor de idade.")

"""
    Imagine que você queira imprimir "Aprovado(a)" caso o estudante tenha uma média
    superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""

"""
media = float(input('Informe a média do estudante: '))

if media >= 7:
    print('Você foi aprovado(a)!')
elif media >= 5:
    print('Recuperação')
else:
    print('Você foi reprovado(a)!')
"""

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovado(a)!')
    print('Parabéns!')
else:
    print('Reprovado(a)!')
    print('Tente novamente!')