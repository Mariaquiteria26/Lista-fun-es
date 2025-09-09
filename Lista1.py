# def saudacao(nome):
#     return(f"Olá, {nome}! Seja bem-vindo ao curso de lógica de programação.")
# print(saudacao("Lohane"))


# def numero(n):
#     if n % 2 == 0:
#         return(f"{n} é par")
#     else:
#         return(f"{n} é ímpar")
# print(numero(4))


# num=int(input("digite o primeiro numero:"))
# nume=int(input("digite o segundo numero:"))
# if num < nume:
#     print(f"{nume} é o maior numero")
# elif nume < num:
#     print(f"{num} é o maior numero")
# else:
#      print("Eles são iguais")
      

# N = int(input("Digite um número: "))
# for i in range(1, 11):
#     print(f"{i} x {N} = {N*i}")


# for i in range(10, -1, -1):
#     print(i)
# print("explodiu")


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


def fatorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado 
print(fatorial(7))