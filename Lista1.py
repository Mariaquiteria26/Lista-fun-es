#Q1

# def saudacao(nome):
#     return(f"Olá, {nome}! Seja bem-vindo ao curso de lógica de programação.")
# print(saudacao("Lohane"))


#Q2

# def numero(n):
#     if n % 2 == 0:
#         return(f"{n} é par")
#     else:
#         return(f"{n} é ímpar")
# print(numero(4))


#Q3

# num=int(input("digite o primeiro numero:"))
# nume=int(input("digite o segundo numero:"))
# if num < nume:
#     print(f"{nume} é o maior numero")
# elif nume < num:
#     print(f"{num} é o maior numero")
# else:
#      print("Eles são iguais")
      

#Q4

# N = int(input("Digite um número: "))
# for i in range(1, 11):
#     print(f"{i} x {N} = {N*i}")


#Q5

# for i in range(10, -1, -1):
#     print(i)
# print("explodiu")


#Q6

# notas = [10.0, 7.9, 3.0, 9.5]
# def media(notas):
#     soma = cont = 0
#     for nota in notas:
#         soma += nota
#         cont += 1
#     return soma / cont
# print(media(notas))


# notas = [10.0, 7.9, 3.0, 9.5]
# def media(notas):
#     return sum(notas) / len(notas)
# print(media(notas))


#Q7

# def fatorial(num):
#     resultado = 1
#     for i in range(1, num + 1):
#         resultado *= i
#     return resultado 
# print(fatorial(7))


#Q8

def vogais(palavra):
    cont = 0
    for letra in palavra:
        if 



#Q9

# numero = randint(1, 20)
# while True:
#     tentativa = int(input("digite um numero: "))
#     if tentativa == numero:
#         print("você acertou, parabéns!")
#         break
#     elif tentativa < numero:
#         print("o número é maior, tente novamente.")
#     else:
#         print("o número é menor, tente novamente.")


#Q10

# cont = 0
# N = int(input("Digite um número: "))
# for i in range(1, N):
#     if i % 2 == 0:
#         cont += i
# print(f"A soma é {cont}")


#Q11

# def calculadora(a, b, op):
#     if op == "+":
#        return a + b 
#     elif op == "-":
#         return a - b
#     elif op == "*":
#         return a * b
#     elif op == "/":
#         return a / b
# print(calculadora(5, 4, "*"))
    

#Q12

# def primo(a):
#     primo = 0
#     for n in range(1, a):
#      if a % n == 0:
#         primo += 1
#     if primo > 2:
#        return "nao é primo"
#     else:
#        return "é primo"
# print(primo(10))


#Q13

