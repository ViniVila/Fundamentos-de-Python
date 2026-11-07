# 1. Receba a idade em anos e imprima em meses, dias, horas e minutos.
#2. Receba ano de nascimento e ano atual. Calcule idade e semanas.
#3. Receba um número e exiba o dobro.
#4. Receba nome, peso e altura. Calcule IMC.
#5. Converta centímetros para polegadas.
#6. Converta polegadas para centímetros.
#7. Receba nome, cargo e salário e acrescente 10%.


#numeros, textos e booleanos
#Entrada
idade = int(input("Digite sua idade:")) #pega o texto e converte para número inteiro

#processamento
idadeEmMeses = idade * 12
idadeEmDias = idade * 365
idadeEmHoras = idadeEmDias * 24
idadeEmMinutos = idadeEmHoras * 60

#saida
print(f"Sua idade em meses é: {idadeEmMeses} meses")
print(f"Sua idade em dias é {idadeEmDias} dias")
print(f"Sua idade em horas é {idadeEmHoras} horas")
print(f"Sua idade em horas é {idadeEmMinutos} minutos")