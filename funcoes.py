# FUNÇÕES

# 1. O que são funções e por que utilizá-las?

# Funções que já foram utilizadas anteriormente:
print() # - Imprime uma mensagem (INT, FLOAT, STR) no console (Terminal, Prompt de Comando)
input() # - Retorna um dado informado pelo usuário (Entrada Padrão) e pode receber uma String
len() # - Recebe uma lista e retorna o tamanho dessa lista
max() # - Retorna o maior valor de uma lista

# 2. Criação de Funções

# Função Inicial
def saudacao():
    print('Seja bem-vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()
saudacao()
saudacao()

# Função com Parâmetros
def saudacao(nome, curso):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Walisson', 'Introdução à Programação')
saudacao('Aluno', 'JavaScript')

# Função com Parâmetros Default
def saudacao(nome, curso='Introdução à Programação'):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('walisson')
saudacao('walisson', 'C++')

# Função com Retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print('O resultado da soma é', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2

resultado = calculadora(10, 20, '-')
print(resultado)