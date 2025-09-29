cont = 0
pessoas = []
for i in range(5):
    nome = input(f"Digite o {i+1}° nome: ")
    pessoas.append(nome)
    if nome[0] in "Aa":
        cont += 1
for pessoas in pessoas:
    print(pessoas)
print(f"Número de pessoas que começam com A é: {cont}")  
    
