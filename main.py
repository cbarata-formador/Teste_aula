""" " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " *
V0.1
Data: 22/July/2025
Autor: Jessica Costa
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " """ 

print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")

idade = int(input("\nQual a sua idade? "))

if idade < 18:
    print("Você é menor de idade\n")
elif idade >= 18:
    print("Você é maior de idade\n")
else:
    print("\nErro, opção inválida! ")     