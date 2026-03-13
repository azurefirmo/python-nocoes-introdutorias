"""for variavel in range(5):
    print(variavel)"""

"""for variavel in range(1, 11):
    print(variavel)"""

# 1, 4, 7, 10
"""for variavel in range(1, 12, 3):
    print(variavel)"""

"""nota1 = float(input('Informe sua 1ª nota: '))
nota2 = float(input('Informe sua 2ª nota: '))
nota3 = float(input('Informe sua 3ª nota: '))"""

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua {i}ª nota: '))
    soma = soma + nota

print(soma / 3)