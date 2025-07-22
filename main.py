""" " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " *
V0.1
Data: 22/July/2025
Autor: Jessica Costa
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " """ 

from datetime import date

def calc_idade(ano, mes, dia):
    hoje = date.today()
    ja_fez_anos = ((hoje.month, hoje.day) < (mes, dia))
    idade = hoje.year - ano - ja_fez_anos
 
    print("\nO Utilizador tem ",idade," anos hoje")
    
    if idade < 10:
        print("\nCriança\n")
    elif idade >= 10 and idade < 18:
        print("\nAdolescente\n")
    elif idade >= 18 and idade < 65:
        print("\nAdulto\n")
    elif idade >= 65:
        print("\nSénior\n")
    else:
        print("\nErro, opção inválida! ")        
    return


print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")

idade = int(input("\Qual a sua idade? "))

if idade < 18:
    print("Você é menor de idade!\n")
elif idade >= 18:
    print("Você é maior de idade!\n")
else:
    print("\nErro, opção inválida! ")     