#2. Receba ano de nascimento ano atual.Calcule idade e semanas.


#Entrada
anoNascimento = int(input("Digite o ano que nasceu:")) 
anoAtual = int(input("Digite o ano atual:"))
#anoNascimento
#anoAtual

#processamento
idade = anoAtual - anoNascimento
idadeSemana = 4 * 12 * idade

#saída

print(f"sua idade é: {idade} anos")
print(f"sua idade em semanas é: {idadeSemana}")