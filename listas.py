# LISTAS

# ANTES
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# AGORA
notas = [7.9, 9.7, 8.2]

# Criando listas
lista = []
lista = list()
lista = [26, 'Walisson', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (Fatiamento)
lista = [10, 'Walisson', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print(lista[4])

print(lista[-1])

# Slices
lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

# Iterações com FOR

# 1. Utilizando os próprios elementos da lista
for elemento in lista:
    print(elemento)

# 2. Utilizando os índices
print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])

# Métodos de Listas

lista1 = [1, 3, 12, 8, 2]

# APPEND
print(lista1)
lista1.append(3)

# INSERT
lista1.insert(2, 10)
print('Depois do INSERT: ', lista1)

# EXTEND
lista2 = [1, 2, 3]
lista1.extend(lista2)
print('Depois do EXTEND: ', lista1)

# POP
lista1.pop()
print('Depois do POP: ', lista1)

lista1.pop(0)
print('Depois do POP: ', lista1)

# REMOVE
lista1.remove(3)
print('Depois do REMOVE: ', lista1)

# COUNT
print('Quantidade de 2 na 1ª lista: ', lista1.count(2))

# INDEX
print('Índice do elemento 12 na lista: ', lista1.index(12))

# SORT
lista1.sort(reverse=True)

print(lista)

# FUNÇÕES PARA LISTAS

# LEN
print(len(lista1))

# SUM
print(sum(lista1))

# MAX
print('Maior elemento da lista: ', max(lista1))

# MIN
print('Menor elemento da lista: ', min(lista1))