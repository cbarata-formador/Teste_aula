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
             
    return idade


 # Início programa   

print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é a sua data de nascimento?")
print(f"Olá, {nome}!")

print("Qual a sua idade? ") 
    
try:
    ano = int(input("Ano: "))
    mes = int(input("Mês: "))
    dia = int(input("Dia: "))
    
    idade = calc_idade(ano, mes, dia)   
    
except ValueError:
    print("\nErro, insira a data correctamente")
    
if idade < 18:
    print("Você é menor de idade!\n")
elif idade >= 18:
    print("Você é maior de idade!\n")
else:
    print("\nErro, opção inválida! ")   